#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2021-2026 Valory AG
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------
"""
Script to check if all submodules are on their latest released versions.
"""

import argparse
import subprocess
import sys
from pathlib import Path


def run_command(cmd, cwd=None, capture_output=True, ignore_errors=False):
    """Run a shell command and return the result."""
    try:
        result = subprocess.run(
            cmd, shell=True, cwd=cwd, capture_output=capture_output, 
            text=True, check=True
        )
        return result.stdout.strip() if capture_output else None
    except subprocess.CalledProcessError as e:
        if ignore_errors:
            return None

        if capture_output:
            print(f"Error running command '{cmd}': {e.stderr}")
        raise


def get_submodules():
    """Get list of submodules in the repository."""
    try:
        run_command('git submodule update --init --recursive')
        output = run_command("git submodule status")
        submodules = []
        for line in output.splitlines():
            if line.strip():
                # Parse submodule status: commit hash, path, and optional info
                parts = line.strip().split()
                if len(parts) < 2:
                    print(f"Warning: Unexpected submodule line format: {line}")
                    continue

                path = parts[1]
                submodules.append(path)

        return submodules
    except subprocess.CalledProcessError:
        return []


def get_current_commit(submodule_path):
    """Get the current commit hash of a submodule."""
    return run_command("git rev-parse HEAD", cwd=submodule_path)


def get_current_tag(submodule_path):
    """Get the current tag of a submodule."""
    return run_command("git describe --tags --abbrev=0", cwd=submodule_path, ignore_errors=True)


def get_remote_url(submodule_path):
    """Get the remote URL of a submodule."""
    return run_command("git remote get-url origin", cwd=submodule_path)


def get_latest_release_tag(submodule_path):
    """Get the latest release tag from the remote repository."""
    try:
        # Fetch latest tags
        run_command("git fetch --tags -f", cwd=submodule_path)
        
        # Get the latest tag that looks like a version
        tags = run_command("git tag -l --sort=-version:refname", cwd=submodule_path)
        
        for tag in tags.splitlines():
            tag = tag.strip()
            if tag and (tag.startswith('v') or tag[0].isdigit()):
                return tag
        else:
            return None

    except subprocess.CalledProcessError:
        return None


def get_commit_for_tag(submodule_path, tag):
    """Get the commit hash for a specific tag."""
    return run_command(f"git rev-list -n 1 {tag}", cwd=submodule_path)


def update_submodule_to_tag(submodule_path, tag):
    """Update submodule to a specific tag."""
    print(f"  Updating {submodule_path} to {tag}...")
    run_command(f"git checkout {tag}", cwd=submodule_path)


def main():
    parser = argparse.ArgumentParser(description="Check submodule release versions")
    parser.add_argument("--fix", action="store_true", 
                       help="Update submodules to latest releases")
    args = parser.parse_args()

    # Check if we're in a git repository
    try:
        run_command("git rev-parse --git-dir")
    except subprocess.CalledProcessError:
        print("Error: Not in a git repository")
        sys.exit(1)

    submodules = get_submodules()
    
    if not submodules:
        print("No submodules found in this repository")
        return

    print(f"Checking {len(submodules)} submodule(s)...")
    
    outdated_submodules = []
    
    for submodule_path in submodules:
        print(f"\nChecking {submodule_path}...")
        
        if not Path(submodule_path).exists():
            print(f"  Warning: Submodule path {submodule_path} does not exist")
            continue
            
        try:
            current_commit = get_current_commit(submodule_path)
            current_tag = get_current_tag(submodule_path)
            latest_tag = get_latest_release_tag(submodule_path)
            
            if not latest_tag:
                print(f"  No release tags found for {submodule_path}")
                continue
                
            latest_commit = get_commit_for_tag(submodule_path, latest_tag)
            
            if not latest_commit:
                print(f"  Could not get commit for tag {latest_tag} in {submodule_path}")
                continue
                
            if current_commit == latest_commit:
                print(f"  ✓ Up to date (on {latest_tag})")
            else:
                print(f"  ✗ Outdated - current: {current_tag if current_tag else 'N/A'} ({current_commit[:8]}), latest: {latest_tag} ({latest_commit[:8]})")
                outdated_submodules.append((submodule_path, latest_tag))
                
        except Exception as e:
            print(f"  Error checking {submodule_path}: {e}")
    
    if outdated_submodules:
        print(f"\n{len(outdated_submodules)} submodule(s) are not on the latest release:")
        for submodule_path, latest_tag in outdated_submodules:
            print(f"  - {submodule_path} (latest: {latest_tag})")
        
        if args.fix:
            print("\nUpdating outdated submodules...")
            for submodule_path, latest_tag in outdated_submodules:
                try:
                    update_submodule_to_tag(submodule_path, latest_tag)
                except Exception as e:
                    print(f"  Error updating {submodule_path}: {e}")

        else:
            print("\nRun with --fix to update them automatically")
            sys.exit(1)
    else:
        print("\n✓ All submodules are on their latest releases")


if __name__ == "__main__":
    main()