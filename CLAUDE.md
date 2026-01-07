# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This repository aggregates documentation for the Olas Stack site (primary documentation for Olas ecosystem). It uses git submodules to pull in documentation from multiple product repositories and combines them into a unified MkDocs site using the monorepo plugin.

## Architecture

### Submodule-Based Documentation

The documentation is composed of multiple git submodules, each representing a different Olas product:

- **Core Frameworks**: `open-autonomy`, `open-aea`, `open-acn`
- **Toolkits/Products**: `mech`, `mech-client`, `mech-tools-dev`, `IEKit`, `price-oracle`
- **Demos**: `hello-world`

Each submodule contains its own `mkdocs.yml` file that is included in the main `mkdocs.yml` via the `!include` directive from the monorepo plugin.

### Documentation Structure

- `docs/` - Main documentation content (index, protocol docs, custom pages)
- `mkdocs.yml` - Main configuration that orchestrates all submodule documentation
- Submodule directories - Each contains documentation for a specific product

The site is built using MkDocs with Material theme and published to GitHub Pages.

## Common Commands

### Initial Setup

```bash
git submodule update --init --recursive
poetry shell
poetry install --no-root
```

### Build and Serve Documentation

```bash
# Build documentation
tox -e docs

# Serve documentation locally (localhost:8000)
tox -e docs-serve
```

### Quality Checks

```bash
# Check copyright headers
tox -e check-copyright

# Fix copyright headers
tox -e fix-copyright

# Check documentation links
tox -e check-doc-links

# Spell check
tox -e spell-check

# Check submodule versions
tox -e check-submodules-versions
```

### Submodule Management

```bash
# Update all submodules to latest tags (used for releases)
make prepare-release

# Generate release message with all submodule versions
make release-message

# Manually update submodules to latest commits on their default branches
git submodule update --remote --merge
```

### Docker

```bash
# Build Docker image
docker build -t 'docs' .

# Run documentation server on localhost:8001
docker run --rm -p 8001:80 docs
```

## Release Process

Releases follow a two-PR pattern:

1. **Submodule Update PR** (`chore/update-submodules-vX.Y.Z`)
   - Run `make prepare-release` to update submodules to their latest tags
   - Each submodule author must verify and approve

2. **Release PR** (`feat/release-X.Y.Z`)
   - Update `HISTORY.md` with submodule versions and changes
   - After merge and release creation, GitHub Actions builds and publishes the Docker image

Version numbering follows the Open Autonomy version with optional patch increments (e.g., v0.13.0.1) for updates between Open Autonomy releases.

## Working with This Repository

### When Modifying Documentation Content

- Most documentation lives in the submodules, not in this repo
- To change submodule documentation, work directly in the source repository and update the submodule reference
- This repository only contains aggregated/cross-cutting documentation in `docs/`

### When Adding New Products

1. Add submodule: `git submodule add <url> <path>`
2. Update `.gitmodules`
3. Add entry to `mkdocs.yml` nav section with `!include` directive
4. Update `Makefile` release-message target if needed

### MkDocs Configuration

- `strict: true` is enabled - broken links will fail the build
- Custom variables are defined in the `extra` section for reuse across docs
- Redirect mappings preserve old URLs when restructuring documentation

### External Dependencies

The site uses several external JavaScript libraries referenced in `extra_javascript`:

- **Mermaid** (v11.4.1): For rendering diagrams - keep updated for security and features
- **MathJax** (v3): For rendering mathematical equations
- **Local scripts**: `mathjax.js` (configuration) and `dynamic-hash.js` (dynamic hash updates)

**Important**: Never add polyfill.io or similar deprecated CDNs. Modern browsers support ES6+ natively. If polyfills are needed, use Cloudflare's mirror or bundle locally.

### CSS and JavaScript Files

- Local CSS: `docs/stylesheets/extra.css` (custom theming)
- Local JS: `docs/javascripts/mathjax.js` and `docs/javascripts/dynamic-hash.js`
- These files are intentionally unminified for maintainability (total ~52 lines)
- External dependencies are already minified via CDN
