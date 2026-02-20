#!/usr/bin/env python3

"""Create a deterministic dependency graph for valory-xyz repositories.

Rules implemented:
1) List all non-archived repos from the target org.
2) Infer dependencies from dependency-oriented files when a repo name or package alias
   (derived from `packages/packages.json` -> `dev` keys) is mentioned.
3) Infer dependencies from `packages/packages.json` where repo B `third_party` keys
   reference repo A `dev` keys.

All remote operations use GitHub API endpoints (and raw download URLs when required),
and repositories are scanned on `main` with fallback to `master`.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import re
import sys
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

try:
    import tomllib
except ModuleNotFoundError:
    try:
        import tomli as tomllib  # type: ignore
    except ModuleNotFoundError:
        tomllib = None  # type: ignore


API_BASE = "https://api.github.com"
RAW_BASE = "https://raw.githubusercontent.com"
DEFAULT_ORG = "valory-xyz"
DEFAULT_OUTPUT = "docs/dependency_graph.md"
DEFAULT_TOKEN_ENV = "GITHUB_TOKEN"

DEPENDENCY_FILE_RE = re.compile(
    r"(^|/)"
    r"(pyproject\.toml|setup\.py|package\.json|Cargo\.toml|go\.mod|Pipfile|remappings\.txt|\.gitmodules)$"
)
REQUIREMENTS_FILE_RE = re.compile(r"(^|/)requirements[^/]*$")
PACKAGES_FILE_PATH = "packages/packages.json"

# Repositories to exclude from the dependency graph
EXCLUDED_REPOS = {
    "academy-learning-service",
    "academy-learning-service-template",
    "academy-solutions",
    "aea-babyagi",
    "airdrop-helper",
    "autonolas-aip",
    "co-owned-ai-website",
    "ethereum-optimism.github.io",
    "press-kit-valory",
}


@dataclass(frozen=True)
class Repo:
    """Repository metadata used by the graph builder."""

    name: str
    default_branch: str


@dataclass(frozen=True)
class RepoContext:
    """Resolved branch and extracted metadata for a repository."""

    repo: Repo
    branch: str
    aliases: Tuple[str, ...]
    dev_keys: Tuple[str, ...]


@dataclass(frozen=True)
class Evidence:
    """Evidence attached to a dependency edge."""

    url: str
    reason: str
    priority: int


class RequestCache:
    """Simple file-based cache for HTTP responses."""

    def __init__(self, use_cache: bool = False, verbose: bool = False) -> None:
        self._use_cache = use_cache
        self._verbose = verbose
        self._cache_dir: Optional[Path] = None
        self._in_memory: Dict[str, object] = {}
        if use_cache:
            cache_dir = Path(tempfile.gettempdir()) / "github-cache"
            cache_dir.mkdir(parents=True, exist_ok=True)
            self._cache_dir = cache_dir
            if verbose:
                print(f"[cache] using directory: {cache_dir}", file=sys.stderr)

    def _cache_key(self, url: str) -> str:
        """Generate deterministic cache key from URL."""
        return hashlib.sha256(url.encode()).hexdigest()

    def get(self, url: str) -> Optional[str]:
        """Retrieve cached response if available."""
        if not self._use_cache:
            return None

        key = self._cache_key(url)
        if key in self._in_memory:
            if self._verbose:
                print(f"[cache-hit] {url[:60]}...", file=sys.stderr)
            return self._in_memory[key]

        if self._cache_dir:
            cache_file = self._cache_dir / key
            if cache_file.exists():
                try:
                    content = cache_file.read_text(encoding="utf-8")
                    self._in_memory[key] = content
                    if self._verbose:
                        print(f"[cache-hit] {url[:60]}...", file=sys.stderr)
                    return content
                except Exception:
                    pass
        return None

    def set(self, url: str, content: str) -> None:
        """Store response in cache."""
        if not self._use_cache:
            return

        key = self._cache_key(url)
        self._in_memory[key] = content

        if self._cache_dir:
            try:
                cache_file = self._cache_dir / key
                cache_file.write_text(content, encoding="utf-8")
                if self._verbose:
                    print(f"[cache-store] {url[:60]}...", file=sys.stderr)
            except Exception:
                pass


class GitHubClient:
    """Thin GitHub API client with deterministic request handling."""

    def __init__(self, token: Optional[str], verbose: bool = False, cache: Optional[RequestCache] = None) -> None:
        self._token = token
        self._verbose = verbose
        self._cache = cache or RequestCache(use_cache=False, verbose=verbose)

    def _headers(self, accept: str = "application/vnd.github+json") -> Dict[str, str]:
        headers = {
            "Accept": accept,
            "User-Agent": "dependency-graph-generator",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if self._token:
            headers["Authorization"] = f"Bearer {self._token}"
        return headers

    def _request(self, url: str, accept: str = "application/vnd.github+json") -> Tuple[bytes, Dict[str, str]]:
        cached = self._cache.get(url)
        if cached is not None:
            return cached.encode("utf-8"), {}

        request = Request(url, headers=self._headers(accept=accept))
        try:
            with urlopen(request, timeout=30) as response:  # nosec B310
                data = response.read()
                headers = {k: v for k, v in response.headers.items()}
                text = data.decode("utf-8", errors="replace")
                self._cache.set(url, text)
                return data, headers
        except HTTPError as exc:
            remaining = exc.headers.get("X-RateLimit-Remaining", "") if exc.headers else ""
            reset = exc.headers.get("X-RateLimit-Reset", "") if exc.headers else ""
            if exc.code in (403, 429) and remaining == "0" and reset:
                sleep_seconds = max(0, int(reset) - int(time.time()) + 1)
                if self._verbose:
                    print(f"[rate-limit] sleeping {sleep_seconds}s for reset", file=sys.stderr)
                time.sleep(sleep_seconds)
                return self._request(url, accept=accept)
            raise
        except URLError:
            raise

    def get_json(self, url: str) -> object:
        payload, _ = self._request(url)
        return json.loads(payload.decode("utf-8"))

    def get_text(self, url: str, accept: str = "application/vnd.github.raw") -> str:
        payload, _ = self._request(url, accept=accept)
        return payload.decode("utf-8", errors="replace")


def normalize_alias(value: str) -> str:
    """Normalize an alias token for deterministic matching."""

    return value.strip().lower().replace("_", "-")


def node_id(repo_name: str) -> str:
    """Create a Mermaid-safe deterministic node id from repository name."""

    cleaned = re.sub(r"[^a-zA-Z0-9_]", "_", repo_name)
    if re.match(r"^[0-9]", cleaned):
        cleaned = f"repo_{cleaned}"
    return cleaned


def branch_for_repo(client: GitHubClient, org: str, repo: str, verbose: bool = False) -> Optional[str]:
    """Return `main`, else `master`, else None."""

    for candidate in ("main", "master"):
        url = f"{API_BASE}/repos/{org}/{repo}/branches/{candidate}"
        try:
            client.get_json(url)
            if verbose:
                print(f"[branch] {repo}: resolved to '{candidate}'", file=sys.stderr)
            return candidate
        except HTTPError as exc:
            if exc.code == 404:
                if verbose:
                    print(f"[branch] {repo}: '{candidate}' not found", file=sys.stderr)
                continue
            raise
    if verbose:
        print(f"[skip] {repo}: no main or master branch found", file=sys.stderr)
    return None


def list_non_archived_repos(client: GitHubClient, org: str, verbose: bool = False) -> List[Repo]:
    """List all non-archived repos in deterministic order."""

    page = 1
    repos: List[Repo] = []
    if verbose:
        print(f"[enumerate] listing non-archived repos from {org}...", file=sys.stderr)
    while True:
        url = (
            f"{API_BASE}/orgs/{org}/repos"
            f"?type=all&sort=full_name&direction=asc&per_page=100&page={page}"
        )
        payload = client.get_json(url)
        if not isinstance(payload, list):
            raise RuntimeError("Unexpected response while listing repositories")
        if not payload:
            break
        for item in payload:
            if item.get("archived", False):
                if verbose:
                    print(f"[skip] {item.get('name')}: archived", file=sys.stderr)
                continue
            name = item.get("name")
            if name in EXCLUDED_REPOS:
                if verbose:
                    print(f"[skip] {name}: excluded", file=sys.stderr)
                continue
            default_branch = item.get("default_branch") or "main"
            if not name:
                continue
            repos.append(Repo(name=name, default_branch=default_branch))
        page += 1
    repos.sort(key=lambda r: r.name.lower())
    if verbose:
        print(f"[enumerate] found {len(repos)} non-archived repos", file=sys.stderr)
    return repos


def list_dependency_files(client: GitHubClient, org: str, repo: str, branch: str, verbose: bool = False) -> List[str]:
    """List dependency-oriented files to scan from a repository tree."""

    tree_url = f"{API_BASE}/repos/{org}/{repo}/git/trees/{quote(branch)}?recursive=1"
    try:
        payload = client.get_json(tree_url)
    except HTTPError as exc:
        if verbose:
            print(f"[skip-tree] {repo}: failed to list tree ({exc.code})", file=sys.stderr)
        return []
    tree = payload.get("tree", []) if isinstance(payload, dict) else []
    paths: Set[str] = set()
    for entry in tree:
        if entry.get("type") != "blob":
            continue
        path = entry.get("path", "")
        if path == PACKAGES_FILE_PATH:
            paths.add(path)
            continue
        if DEPENDENCY_FILE_RE.search(path) or REQUIREMENTS_FILE_RE.search(path):
            paths.add(path)
    result = sorted(paths)
    if verbose and result:
        files_str = ", ".join(result)
        print(f"[files] {repo}: found {len(result)} dependency files: {files_str}", file=sys.stderr)
    return result


def get_file_text(client: GitHubClient, org: str, repo: str, branch: str, path: str) -> Optional[str]:
    """Read file text using contents API, fallback to raw CDN URL."""

    contents_url = f"{API_BASE}/repos/{org}/{repo}/contents/{quote(path)}?ref={quote(branch)}"
    try:
        payload = client.get_json(contents_url)
    except HTTPError as exc:
        if exc.code != 404:
            raise
        return None

    if not isinstance(payload, dict):
        return None

    encoded = payload.get("content")
    encoding = payload.get("encoding")
    if encoded and encoding == "base64":
        decoded = base64.b64decode(encoded)
        return decoded.decode("utf-8", errors="replace")

    download_url = payload.get("download_url")
    if download_url:
        try:
            return client.get_text(download_url, accept="application/vnd.github.raw")
        except HTTPError:
            return None

    raw_url = f"{RAW_BASE}/{org}/{repo}/{quote(branch)}/{path}"
    try:
        return client.get_text(raw_url, accept="application/octet-stream")
    except HTTPError:
        return None


def parse_packages_json(text: Optional[str]) -> Tuple[Set[str], Set[str]]:
    """Parse `dev` and `third_party` keys from packages/packages.json content."""

    if not text:
        return set(), set()
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        return set(), set()

    dev = payload.get("dev", {}) if isinstance(payload, dict) else {}
    third_party = payload.get("third_party", {}) if isinstance(payload, dict) else {}

    dev_keys = {normalize_alias(key) for key in dev.keys()} if isinstance(dev, dict) else set()
    third_party_keys = (
        {normalize_alias(key) for key in third_party.keys()} if isinstance(third_party, dict) else set()
    )
    return dev_keys, third_party_keys


def build_repo_contexts(client: GitHubClient, org: str, repos: Iterable[Repo], verbose: bool) -> Tuple[List[RepoContext], Dict[str, Set[str]], Dict[str, Set[str]]]:
    """Resolve branches and collect aliases/dev/third_party package data."""

    contexts: List[RepoContext] = []
    repo_dev: Dict[str, Set[str]] = {}
    repo_third_party: Dict[str, Set[str]] = {}

    if verbose:
        print(f"[resolve] building repo contexts...", file=sys.stderr)

    for repo in repos:
        branch = branch_for_repo(client, org, repo.name, verbose=verbose)
        if branch is None:
            continue

        packages_text = get_file_text(client, org, repo.name, branch, PACKAGES_FILE_PATH)
        dev_keys, third_party_keys = parse_packages_json(packages_text)
        
        if verbose:
            if packages_text:
                print(f"[parse] {repo.name}: {len(dev_keys)} dev keys, {len(third_party_keys)} third_party keys", file=sys.stderr)
            else:
                print(f"[parse] {repo.name}: no packages.json or empty", file=sys.stderr)
        
        aliases = {
            normalize_alias(repo.name),
            normalize_alias(repo.name.replace("-", "_")),
            normalize_alias(repo.name.replace("_", "-")),
        }
        aliases.update(dev_keys)

        repo_dev[repo.name] = set(dev_keys)
        repo_third_party[repo.name] = set(third_party_keys)
        contexts.append(
            RepoContext(
                repo=repo,
                branch=branch,
                aliases=tuple(sorted(aliases)),
                dev_keys=tuple(sorted(dev_keys)),
            )
        )

    contexts.sort(key=lambda c: c.repo.name.lower())
    if verbose:
        print(f"[resolve] built {len(contexts)} repo contexts", file=sys.stderr)
    return contexts, repo_dev, repo_third_party


def first_line_for_alias(text: str, aliases: Iterable[str]) -> Optional[int]:
    """Find first line containing any alias using token boundaries."""

    patterns = [
        re.compile(rf"(?<![a-z0-9]){re.escape(alias)}(?![a-z0-9])")
        for alias in aliases
    ]
    for index, line in enumerate(text.splitlines(), start=1):
        lowered = line.lower()
        for pattern in patterns:
            if pattern.search(lowered):
                return index
    return None


def extract_dependencies_from_toml(text: str) -> List[str]:
    """Extract dependency package names from pyproject.toml."""
    if tomllib is None:
        return []
    
    try:
        data = tomllib.loads(text)
    except Exception:
        return []
    
    deps = set()
    
    # Poetry format
    if "tool" in data and "poetry" in data["tool"]:
        poetry = data["tool"]["poetry"]
        if "dependencies" in poetry and isinstance(poetry["dependencies"], dict):
            for key in poetry["dependencies"].keys():
                if key != "python":
                    deps.add(key)
        if "dev-dependencies" in poetry and isinstance(poetry["dev-dependencies"], dict):
            for key in poetry["dev-dependencies"].keys():
                deps.add(key)
    
    # PEP 621 format
    if "project" in data and "dependencies" in data["project"]:
        if isinstance(data["project"]["dependencies"], list):
            for dep in data["project"]["dependencies"]:
                pkg_name = dep.split(";")[0].split("[")[0].split("=")[0].split("<")[0].split(">")[0].split("!")[0].split("~")[0].strip()
                if pkg_name:
                    deps.add(pkg_name)
    
    return sorted(deps)


def extract_dependencies_from_pipfile(text: str) -> List[str]:
    """Extract dependency package names from Pipfile."""
    if tomllib is None:
        return []
    
    try:
        data = tomllib.loads(text)
    except Exception:
        return []
    
    deps = set()
    
    # Extract from [packages] section
    if "packages" in data and isinstance(data["packages"], dict):
        deps.update(data["packages"].keys())
    
    # Extract from [dev-packages] section
    if "dev-packages" in data and isinstance(data["dev-packages"], dict):
        deps.update(data["dev-packages"].keys())
    
    return sorted(deps)


def extract_dependencies_from_setup_py(text: str) -> List[str]:
    """Extract dependency package names from setup.py using regex."""
    deps = set()
    
    # First, try to find install_requires as a literal list
    install_match = re.search(r'install_requires\s*=\s*\[(.*?)\]', text, re.DOTALL)
    if install_match:
        content = install_match.group(1)
        for match in re.finditer(r'"([^"]+)"|\'([^\']+)\'', content):
            pkg = match.group(1) or match.group(2)
            pkg_name = pkg.split(";")[0].split("[")[0].split("=")[0].split("<")[0].split(">")[0].split("!")[0].split("~")[0].strip()
            if pkg_name:
                deps.add(pkg_name)
        return sorted(deps)
    
    # If not found, try to find install_requires pointing to a variable
    var_match = re.search(r'install_requires\s*=\s*([a-zA-Z_][a-zA-Z0-9_]*)', text)
    if var_match:
        var_name = var_match.group(1)
        # Find the variable definition and extract all strings from it
        # This regex looks for: var_name = [ ... ] and captures everything between brackets
        var_pattern = rf'{re.escape(var_name)}\s*=\s*\[(.*?)\](?=\n|$)'
        var_match_content = re.search(var_pattern, text, re.DOTALL)
        if var_match_content:
            content = var_match_content.group(1)
            for match in re.finditer(r'"([^"]+)"|\'([^\']+)\'', content):
                pkg = match.group(1) or match.group(2)
                pkg_name = pkg.split(";")[0].split("[")[0].split("=")[0].split("<")[0].split(">")[0].split("!")[0].split("~")[0].strip()
                if pkg_name:
                    deps.add(pkg_name)
    
    return sorted(deps)


def extract_dependencies_from_package_json(text: str) -> List[str]:
    """Extract dependency package names from package.json."""
    try:
        data = json.loads(text)
    except Exception:
        return []
    
    deps = set()
    
    # Regular dependencies
    if "dependencies" in data and isinstance(data["dependencies"], dict):
        deps.update(data["dependencies"].keys())
    
    # Dev dependencies
    if "devDependencies" in data and isinstance(data["devDependencies"], dict):
        deps.update(data["devDependencies"].keys())
    
    return sorted(deps)


def extract_dependencies_from_requirements(text: str) -> List[str]:
    """Extract dependency package names from requirements.txt."""
    deps = set()
    
    for line in text.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # Remove comments and version specs
        pkg_name = line.split(";")[0].split("[")[0].split("=")[0].split("<")[0].split(">")[0].split("!")[0].split("~")[0].strip()
        if pkg_name:
            deps.add(pkg_name)
    
    return sorted(deps)


def extract_dependencies_from_remappings(text: str) -> List[str]:
    """Extract dependency package names from remappings.txt (Solidity/Foundry)."""
    deps = set()
    
    for line in text.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        
        # Parse remapping format: @package/=path or package/=path
        # Examples: @openzeppelin/=node_modules/@openzeppelin/
        #           forge-std/=lib/forge-std/src/
        if "=" in line:
            left_side = line.split("=")[0].strip()
            # Remove leading @ and trailing /
            pkg_name = left_side.lstrip("@").rstrip("/")
            if pkg_name:
                deps.add(pkg_name)
    
    return sorted(deps)


def extract_dependencies_from_gitmodules(text: str) -> List[str]:
    """Extract dependency repository names from .gitmodules."""
    deps = set()
    
    # Parse .gitmodules format:
    # [submodule "name"]
    #     path = path/to/submodule
    #     url = https://github.com/org/repo.git
    
    lines = text.split("\n")
    current_url = None
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        
        # Look for url = ... lines
        if line.startswith("url"):
            match = re.search(r'url\s*=\s*(.+)', line)
            if match:
                url = match.group(1).strip()
                # Extract repo name from various URL formats:
                # https://github.com/org/repo.git -> repo
                # git@github.com:org/repo.git -> repo
                # https://github.com/org/repo -> repo
                
                # Remove .git suffix
                url = url.rstrip(".git")
                
                # Extract last part of path
                if "/" in url:
                    repo_name = url.split("/")[-1]
                elif ":" in url:
                    # Handle git@github.com:org/repo format
                    repo_name = url.split(":")[-1].split("/")[-1]
                else:
                    repo_name = url
                
                if repo_name:
                    deps.add(repo_name)
    
    return sorted(deps)


def find_alias_mentions(text: str, aliases: Iterable[str]) -> bool:
    """Return True if any alias is found using strict token boundaries."""

    lowered = text.lower()
    for alias in aliases:
        pattern = re.compile(rf"(?<![a-z0-9\-]){re.escape(alias)}(?![a-z0-9\-])")
        if pattern.search(lowered):
            return True
    return False


def infer_edges_from_mentions(
    client: GitHubClient,
    org: str,
    contexts: Iterable[RepoContext],
    verbose: bool,
) -> Dict[Tuple[str, str], Evidence]:
    """Infer dependencies by extracting actual dependencies from dependency files."""

    contexts_list = list(contexts)
    alias_map = {ctx.repo.name: set(ctx.aliases) for ctx in contexts_list}
    edges: Dict[Tuple[str, str], Evidence] = {}

    if verbose:
        print(f"[infer-mentions] scanning {len(contexts_list)} repos for dependencies...", file=sys.stderr)

    for idx, source_ctx in enumerate(contexts_list, start=1):
        files = list_dependency_files(client, org, source_ctx.repo.name, source_ctx.branch, verbose=verbose)
        if not files:
            if verbose:
                print(f"[scan] {source_ctx.repo.name} ({idx}/{len(contexts_list)}): no dependency files found", file=sys.stderr)
            continue
        
        matches_found = 0
        for path in files:
            text = get_file_text(client, org, source_ctx.repo.name, source_ctx.branch, path)
            if text is None:
                if verbose:
                    print(f"[fetch-fail] {source_ctx.repo.name}/{path}: unable to read", file=sys.stderr)
                continue
            if source_ctx.repo.name == "docs" and path == DEFAULT_OUTPUT:
                if verbose:
                    print(f"[skip] {source_ctx.repo.name}/{path}: skipping self-reference", file=sys.stderr)
                continue
            
            # Extract dependencies based on file type
            file_deps: List[str] = []
            if path.endswith("pyproject.toml"):
                file_deps = extract_dependencies_from_toml(text)
            elif path.endswith("setup.py"):
                file_deps = extract_dependencies_from_setup_py(text)
            elif path.endswith("package.json"):
                file_deps = extract_dependencies_from_package_json(text)
            elif path.endswith("Pipfile"):
                file_deps = extract_dependencies_from_pipfile(text)
            elif path.endswith("remappings.txt"):
                file_deps = extract_dependencies_from_remappings(text)
            elif path.endswith(".gitmodules"):
                file_deps = extract_dependencies_from_gitmodules(text)
            elif path.startswith("requirements"):
                file_deps = extract_dependencies_from_requirements(text)
            elif path == PACKAGES_FILE_PATH:
                # For packages.json, just use raw text scanning (already handled by Rule B)
                continue
            
            # Normalize dependencies for matching
            file_deps_normalized = {normalize_alias(dep) for dep in file_deps}
            
            # Check if any target repo's aliases match extracted dependencies
            for target_ctx in contexts_list:
                if target_ctx.repo.name == source_ctx.repo.name:
                    continue
                target_aliases = alias_map[target_ctx.repo.name]
                target_aliases_normalized = {normalize_alias(alias) for alias in target_aliases}
                
                # Check if there's any intersection
                if not file_deps_normalized.intersection(target_aliases_normalized):
                    continue
                
                # Find line number for evidence URL
                line = first_line_for_alias(text, target_aliases)
                if line is None:
                    continue
                
                url = (
                    f"https://github.com/{org}/{source_ctx.repo.name}/blob/"
                    f"{source_ctx.branch}/{path}#L{line}"
                )
                key = (source_ctx.repo.name, target_ctx.repo.name)
                evidence = Evidence(url=url, reason="mention", priority=20)
                current = edges.get(key)
                if current is None or (evidence.priority, evidence.url) > (current.priority, current.url):
                    edges[key] = evidence
                    matches_found += 1
                    if verbose:
                        print(f"[edge] {source_ctx.repo.name} -> {target_ctx.repo.name} (via {path}:{line})", file=sys.stderr)
        
        if verbose:
            print(f"[scan] {source_ctx.repo.name} ({idx}/{len(contexts_list)}): {len(files)} files, {matches_found} edges inferred", file=sys.stderr)
    
    if verbose:
        print(f"[infer-mentions] {len(edges)} edges from mentions", file=sys.stderr)
    return edges


def infer_edges_from_packages(
    client: GitHubClient,
    org: str,
    contexts: Iterable[RepoContext],
    repo_dev: Dict[str, Set[str]],
    repo_third_party: Dict[str, Set[str]],
    verbose: bool = False,
) -> Dict[Tuple[str, str], Evidence]:
    """Infer dependencies by matching `third_party` keys against `dev` keys."""

    contexts_by_name = {ctx.repo.name: ctx for ctx in contexts}
    edges: Dict[Tuple[str, str], Evidence] = {}

    if verbose:
        print(f"[infer-packages] matching third_party keys to dev keys...", file=sys.stderr)

    for source_repo, third_party_keys in sorted(repo_third_party.items()):
        source_ctx = contexts_by_name.get(source_repo)
        if source_ctx is None:
            continue

        packages_text = get_file_text(
            client,
            org,
            source_repo,
            source_ctx.branch,
            PACKAGES_FILE_PATH,
        )
        packages_payload: Dict[str, object] = {}
        if packages_text:
            try:
                packages_payload = json.loads(packages_text)
            except json.JSONDecodeError:
                packages_payload = {}
        third_party_raw = []
        if isinstance(packages_payload, dict):
            third_party_raw = list((packages_payload.get("third_party") or {}).keys())
        
        local_edges = 0
        for target_repo, dev_keys in sorted(repo_dev.items()):
            if source_repo == target_repo or not dev_keys:
                continue
            intersection = third_party_keys.intersection(dev_keys)
            if intersection:
                key = (source_repo, target_repo)
                matched_raw = [
                    key_name for key_name in third_party_raw if normalize_alias(key_name) in intersection
                ]
                line = None
                if packages_text and matched_raw:
                    line = first_line_for_alias(packages_text, matched_raw)
                url = (
                    f"https://github.com/{org}/{source_repo}/blob/"
                    f"{source_ctx.branch}/{PACKAGES_FILE_PATH}"
                )
                if line:
                    url = f"{url}#L{line}"
                edges[key] = Evidence(url=url, reason="packages", priority=10)
                local_edges += 1
                if verbose:
                    print(f"[edge] {source_repo} -> {target_repo} (packages: {', '.join(sorted(intersection))})", file=sys.stderr)
        
        if verbose and local_edges > 0:
            print(f"[packages] {source_repo}: {local_edges} edges from packages.json", file=sys.stderr)
    
    if verbose:
        print(f"[infer-packages] {len(edges)} edges from packages", file=sys.stderr)
    return edges


def merge_edges(*edge_maps: Dict[Tuple[str, str], Evidence]) -> Dict[Tuple[str, str], Evidence]:
    """Merge edge maps with deterministic evidence preference."""

    merged: Dict[Tuple[str, str], Evidence] = {}
    for edge_map in edge_maps:
        for key, evidence in edge_map.items():
            current = merged.get(key)
            if current is None or (evidence.priority, evidence.url) > (current.priority, current.url):
                merged[key] = evidence
    return merged


def render_graph(org: str, contexts: Iterable[RepoContext], edges: Dict[Tuple[str, str], Evidence]) -> str:
    """Render deterministic Markdown with Mermaid graph."""

    contexts_list = sorted(contexts, key=lambda c: c.repo.name.lower())
    name_to_id = {ctx.repo.name: node_id(ctx.repo.name) for ctx in contexts_list}

    lines: List[str] = [
        "# Valory-xyz Repository Dependency Graph",
        "",
        "```mermaid",
        "flowchart LR",
        "",
        "    %% Nodes",
    ]

    for ctx in contexts_list:
        nid = name_to_id[ctx.repo.name]
        label = ctx.repo.name.replace('"', '\\"')
        lines.append(f'    {nid}["{label}"]')

    lines.extend(["", "    %% Click events"])
    
    for ctx in contexts_list:
        nid = name_to_id[ctx.repo.name]
        repo_url = f"https://github.com/{org}/{ctx.repo.name}"
        lines.append(f'    click {nid} "{repo_url}" _blank')

    lines.extend(["", "    %% Dependencies"])

    for source, target in sorted(edges.keys(), key=lambda item: (item[0].lower(), item[1].lower())):
        source_id = name_to_id[source]
        target_id = name_to_id[target]
        url = edges[(source, target)].url.replace('"', "%22")
        lines.append(
            f'    {source_id} -->|<a href="{url}" target="_blank">Link</a>| {target_id}'
        )

    lines.extend(["", "```", ""])
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""

    parser = argparse.ArgumentParser(description="Generate deterministic repository dependency graph")
    parser.add_argument("--org", default=DEFAULT_ORG, help="GitHub organization name")
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT,
        help="Output markdown file path",
    )
    parser.add_argument(
        "--token-env",
        default=DEFAULT_TOKEN_ENV,
        help="Environment variable holding GitHub token",
    )
    parser.add_argument("--cache", action="store_true", help="Cache network responses in temporary directory")
    parser.add_argument("--dry-run", action="store_true", help="Print output instead of writing file")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    return parser.parse_args()


def main() -> int:
    """Entrypoint."""

    args = parse_args()
    token = os.environ.get(args.token_env)
    cache = RequestCache(use_cache=args.cache, verbose=args.verbose)
    client = GitHubClient(token=token, verbose=args.verbose, cache=cache)

    if args.verbose:
        print(f"[start] generating dependency graph for {args.org}", file=sys.stderr)

    repos = list_non_archived_repos(client=client, org=args.org, verbose=args.verbose)
    if args.verbose:
        print(f"[repos] enumerated {len(repos)} repositories", file=sys.stderr)

    contexts, repo_dev, repo_third_party = build_repo_contexts(
        client=client,
        org=args.org,
        repos=repos,
        verbose=args.verbose,
    )

    if args.verbose:
        repos_with_main_master = len(contexts)
        skipped_count = len(repos) - repos_with_main_master
        print(f"[contexts] {repos_with_main_master} repos have main/master ({skipped_count} skipped)", file=sys.stderr)

    if args.verbose:
        print(f"[infer] starting dependency inference...", file=sys.stderr)

    package_edges = infer_edges_from_packages(
        client=client,
        org=args.org,
        contexts=contexts,
        repo_dev=repo_dev,
        repo_third_party=repo_third_party,
        verbose=args.verbose,
    )
    mention_edges = infer_edges_from_mentions(
        client=client,
        org=args.org,
        contexts=contexts,
        verbose=args.verbose,
    )
    edges = merge_edges(package_edges, mention_edges)

    if args.verbose:
        print(f"[merge] {len(package_edges)} package edges + {len(mention_edges)} mention edges = {len(edges)} total", file=sys.stderr)

    output = render_graph(org=args.org, contexts=contexts, edges=edges)

    if args.verbose:
        print(f"[render] graph rendered ({len(output)} bytes)", file=sys.stderr)

    if args.dry_run:
        if args.verbose:
            print(f"[dry-run] output (first 500 bytes):", file=sys.stderr)
        print(output)
        return 0

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(output, encoding="utf-8")
    
    if args.verbose:
        print(f"[write] {output_path}", file=sys.stderr)
        print(f"[summary] {len(contexts)} repos, {len(edges)} edges, {len(output)} bytes", file=sys.stderr)
        print(f"[complete] dependency graph generated", file=sys.stderr)


if __name__ == "__main__":
    sys.exit(main())
