# docs

This repository aggregates the documentation of all the Autonolas ecosystem products. This repository aggregates the documentation of all the Autonolas ecosystem products.

## Requirements

* Python >= 3.10
* [Poetry](https://python-poetry.org/) >= 1.1.12

## Usage

```bash
git submodule update --init --recursive
poetry shell
poetry install --no-root
mkdocs serve
```

or

```bash
mkdocs build --clean --strict
```
