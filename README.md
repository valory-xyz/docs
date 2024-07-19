# Autonolas Developer Documentation

This repository aggregates the documentation of all the Autonolas ecosystem products.

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
    * **Branch:** `chore/update-submodules-vX.Y.Z`
    * **Title:** "Update submodules"
    * **Contents:** Submodules point to the required commit (typically, it will be the latest release for each submodule). The command `make prepare-release` updates submodules to their latest tag.
    * **Approval:** The PR should be verified and approved by each submodule author.

2. Release PR (see an example [here](https://github.com/valory-xyz/docs/pull/28)):
   * **Branch:** `feat/release-X.Y.Z`
   * **Title:** "Prepare for release vX.Y.Z"
   * **Contents:** Update file `HISTORY.md` with the correct versions of the submodules or any other relevant change.

3. (Optional) Test the Docker image locally:

    ```bash
    docker build -t 'docs' .
    docker run --rm -p 8001:80 docs
    ```

    Test the website with your browser on `http://localhost:8001`.

4. Create release (see an example [here](https://github.com/valory-xyz/docs/releases/tag/v0.10.0)):
   * **Tag:** vX.Y.Z
   * **Title:** vX.Y.Z
   * **Contents:** Latest entry in `HISTORY.md`

5. Publish the release. The hash of the created Docker image containing the documentation site can be found on the release workflow (Build Images workflow / Docker Push).

Notes:

* Occasionally, Step 1 can be merged into Step 2 above. That is, a single PR "Update submodules & Prepare for release vX.Y.Z".
* Since this repository aggregates several submodules that might be updated independently, the versioning of this repository follows the convention of using version number of Open Autonomy repository. Updates of this repository between releases of Open Autonomy will append a number starting at .1 (for example, v0.13.0**.1**, v0.12.1.post4**.1**, etc.)
