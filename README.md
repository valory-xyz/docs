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
tox -e docs-serve
```

or

```bash
tox -e docs
```

## Release process

1. Submodule update PR (see an example [here](https://github.com/valory-xyz/docs/pull/27)):
	* **Branch:** `chore/update_submodules-vX.Y.Z`
	* **Title:** "Update submodules"
	* **Contents:** Submodules point to the required commit (typically, it will be the latest release for each submodule). The command `make prepare-release` updates submodules to their latest tag.
	* **Approval:** The PR should be verified and approved by each submodule author.

2. Release PR (see an example [here](https://github.com/valory-xyz/docs/pull/28)):
   * **Branch:** `feat/release-X.Y.Z`
   * **Title:** "Prepare for release vX.Y.Z"
   * **Contents:** Update file `HISTORY.md` with the correct versions of the submodules or any other relevant change.

3. Create release (see an example [here](https://github.com/valory-xyz/docs/releases/tag/v0.10.0)):
   * **Tag:** vX.Y.Z
   * **Title:** vX.Y.Z
   * **Contents:** Latest entry in `HISTORY.md`

4. Publish the release. The hash of the created Docker image can be found on the release workflow. See an example [here](https://github.com/valory-xyz/docs/actions/runs/4536574834/jobs/7993431764#step:8:24).
