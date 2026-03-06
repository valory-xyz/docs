# Contributing to Olas Stack Documentation

Thank you for your interest in contributing to the Olas Stack documentation! This guide will help you get started.

## Prerequisites

- Python >=3.10
- [Poetry](https://python-poetry.org/) for dependency management
- Git

## Getting Started

1. **Fork and clone** the repository:

   ```bash
   git clone https://github.com/<your-username>/docs.git
   cd docs
   ```

2. **Initialize submodules:**

   ```bash
   git submodule update --init --recursive
   ```

3. **Install dependencies:**

   ```bash
   poetry install --no-root
   poetry shell
   ```

4. **Create a feature branch:**

   ```bash
   git checkout -b feat/your-feature
   ```

## Development Workflow

### Building and Serving Documentation Locally

```bash
# Build the documentation
tox -e docs

# Serve locally at http://localhost:8000
tox -e docs-serve
```

### Running Quality Checks

All checks **must pass** before opening a PR.

```bash
# Check copyright headers
tox -e check-copyright

# Check documentation links
tox -e check-doc-links

# Spell check
tox -e spell-check

# Check submodule versions
tox -e check-submodules-versions
```

To fix copyright headers automatically:

```bash
tox -e fix-copyright
```

### Docker

```bash
# Build Docker image
docker build -t 'docs' .

# Run documentation server on localhost:8001
docker run --rm -p 8001:80 docs
```

## Repository Structure

```
docs/
├── docs/                # Main documentation content (index, custom pages)
│   ├── stylesheets/     # Custom CSS
│   └── javascripts/     # Custom JS (MathJax config, dynamic hash)
├── scripts/             # Quality check scripts (copyright, links, spelling)
├── mkdocs.yml           # Main MkDocs config (orchestrates all submodules)
├── tox.ini              # Tox environments for build and checks
├── Makefile             # Release preparation targets
└── <submodules>/        # Product documentation submodules
    ├── open-autonomy/
    ├── open-aea/
    ├── open-acn/
    ├── mech/
    ├── mech-client/
    ├── mech-server/
    ├── IEKit/
    ├── price-oracle/
    └── hello-world/
```

## Working with Submodules

Most documentation content lives in the submodules, not in this repository. To modify product-specific documentation, work directly in the source repository and update the submodule reference here.

This repository contains only aggregated and cross-cutting documentation in the `docs/` directory.

### Adding a New Product

1. Add submodule: `git submodule add <url> <path>`
2. Update `.gitmodules`
3. Add entry to `mkdocs.yml` nav section with the `!include` directive
4. Update the `Makefile` release-message target if needed

## Code Style and Conventions

- **MkDocs strict mode** is enabled — broken links will fail the build.
- **External JS libraries** (Mermaid, MathJax) are loaded via CDN. Never add `polyfill.io` or similar deprecated CDNs.
- **Local CSS/JS files** are intentionally unminified for maintainability.
- **Copyright headers** are required on applicable files — use `tox -e fix-copyright` to add them.

## Creating a Pull Request

- **Target branch**: Ensure the PR is opened against the correct base branch.
- **Branch naming**: Use kebab-case with a prefix, e.g. `feat/some-feature`, `fix/some-bug`, `docs/update-content`.
- **Link issues**: Reference the relevant ticket or issue in the PR description.
- **Label the PR**: Add appropriate labels such as `enhancement`, `bug`, or `documentation`.
- **Write a clear description**: Explain the purpose and context of the changes.
- **Code review**: Two reviewers will be assigned to each PR.

### PR Checklist

Before pushing, run through this:

```bash
# 1. Fix copyright headers
tox -e fix-copyright

# 2. Run all quality checks
tox -e check-copyright
tox -e check-doc-links
tox -e spell-check

# 3. Build docs to verify
tox -e docs
```

## Reporting Issues

- Use [GitHub Issues](https://github.com/valory-xyz/docs/issues) to report bugs or request improvements.
- Include steps to reproduce, expected behavior, and actual behavior.
- For broken links or rendering issues, mention the specific page URL.

## License

By contributing, you agree that your contributions will be licensed under the [Apache License 2.0](./LICENSE).
