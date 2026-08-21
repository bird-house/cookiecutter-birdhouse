Changelog
=========

..
    `Unreleased <https://github.com/bird-house/cookiecutter-birdhouse>`_ (latest)
    -----------------------------------------------------------------------------
    Contributors:

    Changes
    ^^^^^^^
    * No change.

    Fixes
    ^^^^^
    * No change.

.. _changes_2.1.0:

`v2.1.0 <https://github.com/bird-house/cookiecutter-birdhouse/tree/v2.1.0>`_  (2026-08-20)
------------------------------------------------------------------------------------------

Template changes:

* `CI` folder Python requirements files are now in `.github`. (#168).
* The `pyproject.toml` now lists project information higher. (#168).
* `zizmor` has been added to `pre-commit` hooks. (#168).
* A new Dependabot "auto-accept patch and minor dependency changes" workflow has been added. (#168).
* A new workflow for building and publishing Docker images has been added. (#168).
* Dependabot is now configured to perform updates to pins of base images. (#168).
* The base image for Docker images has migrated from the deprecated `continuumio/miniconda3` to the maintained `condaforge/miniforge3`. (#168).
* Docker metadata is now much more descriptive, with versioning and author information now listed. (#168).
* `bump-my-version` now manages date and version information in Docker image. (#168).
* Guidelines on how to use `bump-my-version` to perform updates and deployments have been added. (#168).
* ReadTheDocs Ubuntu and Python distributions have both been updated. (#168).
* The expected default branch is now `main`. (#168).
* Rendered documentation now uses a dynamic date variable to ensure year is up-to-date (as of last build). (#168).
* `flit` and `flit-core` are now both pinned below v4.0 (due to breaking changes). (#168).
* Added new files (#168):
    * `CITATION.cff`: For citing software directly from GitHub.
    * `.zenodo.json`: For archiving software on Zenodo.

Top-level changes:

* `CI` folder Python requirements files are now in `.github`. (#168).
* The `pyproject.toml` now lists project information higher. (#168).
* `zizmor` has been added to `pre-commit` hooks. (#168).
* The documentation has been slightly adjusted to better reflect the current state of the template. (#168).
* The cookiecutter now has prompts describing each field when generating a new project. (#168).
* Documentation formatting/rendering is nicer. (#168).
* Added a prompt for `ORCID` number. (#168).

.. _changes_2.0.0:

`v2.0.0 <https://github.com/bird-house/cookiecutter-birdhouse/tree/v2.0.0>`_  (2026-06-02)
------------------------------------------------------------------------------------------

Template changes:

* PyPy3.10 support has been dropped. (#143).
* `pyproject.toml` now uses PEP 639 for licensing metadata standards. (#162).
* `pyproject.toml` now uses PEP 735 (dependency-groups) for managing non-package docs, linting, and testing dependencies. (#162).
* Removed `black`, `isort` and `pylint` in favour of `ruff`. (#162).
* Minimum supported Python for generated projects is now 3.11. (#162).
* `pre-commit` has been replaced with `prek`. All hooks have been updated. Added `codespell`, `gitleaks`, and `zizmor`. Removed `black`, `isort`, and duplicated `pygrep` hooks. (#162)
* Renamed `CHANGES.rst` to `CHANGELOG.rst` (more conventional naming). (#162).
* Conda environment configurations no longer use `defaults` (due to licensing issues). (#162).
* ReadTheDocs configuration now uses latest Ubuntu and Conda images. (#162).
* Makefile now uses `dependency-groups` conventions for installing necessary dependencies. (#162).
* Package-building now relies entirely on `flit`. (#162).
* `bump-my-version` updated. New configurations (#162):
    * Now handles entries in `CHANGELOG.rst` when bumping `release`.
    * Now tracks development versions (`-dev.#`).
    * No longer tags commits by default.
* `pytest` updated to v9.0. Uses modern configuration entry. (#162).
* `tox` now uses the TOML configuration. (#162).
* Replace `addnab/docker-run-action` with a good, old-fashioned docker call. (#162).
* Constrained the token-creation actions not to generate tokens with more permissions that required. (#162).

Top-level changes:

* GitHub Actions updatess are now managed using an automated workflow for merging patch and minor changes. (#154).
* `pyproject.toml` now uses PEP 735 (dependency-groups) for managing non-package docs, linting, and testing dependencies. (#162).
* `tox` configuration now found in `pyproject.toml`. (#162).
* README updates. (#162).
* Now uses `prek` for a handful of QA checks. (#162).
* More tests are enabled for PyPy-based template generation. (#162).

.. _changes_1.1.0:

`v1.1.0 <https://github.com/bird-house/cookiecutter-birdhouse/tree/v1.1.0>`_  (2025-02-04)
------------------------------------------------------------------------------------------

Changes:

* Fixed a bug the Dockerfile configuration. (hotfix)
* Added several workflows to help with testing, docker images, and version bumping. (#129).
* Reorganized README files to organize badges better. (#129).
* Added several pre-commit hooks to help with code organization, docstrings, finding dead code blocks, etc. (#129).
* Dropped support for Python3.9, extended support for Python3.13. (#129).
* Now using a CI folder for managing CI-specific Python dependencies.(#129).
* Updated several development dependencies. (#129).
* Now using a Dependabot configuration for managing Python and GitHub Actions updates. (#129).

.. _changes_1.0.0:

`v1.0.0 <https://github.com/bird-house/cookiecutter-birdhouse/tree/v1.0.0>`_  (2024-10-03)
------------------------------------------------------------------------------------------

Changes:

* Replace `search` by `parse` in the bumpversion config for `docs/conf.py` to support the `version|release` expression. (#107, #108).
* Dropped Travis CI and migrated to using GitHub Actions for CI/CD (#112).
* Updated PyWPS to 4.5.0 (#112).
* Ported upstream changes from `cookiecutter-pypackage` and re-enabled testing (#115).
* Added a Makefile command for running `nb-val` with `lax` flags (#116).
* Updated the package metadata to reflect the current state of the project (#117).
* Dropped support for Python2 as well as Python3.8 and below (#120).
* Top-level documentation has been updated to reflect the changes in the project (#120).
* Now using `bump-my-version` for version management and `pre-commit` for code formatting (#120).
* Projects now use a `src`-based directory structure (#120).
* Both the top-level package and rendered templates are now PEP 517 and PEP 621 compliant (`pyproject.toml`) (#120).

.. _changes_0.5.0:

`v0.5.0 <https://github.com/bird-house/cookiecutter-birdhouse/tree/v0.5.0>`_  (2020-10-07)
------------------------------------------------------------------------------------------

Changes:

* Easier to deploy new template to existing project using cruft (#85, #61).
* Use pip instead of setup.py (#97).
* Added conda forge, Python3.8, and osx build (#38).
* Backported fixes from birds (#86, #88, #89).
* Other fixes (#92, #93, #96, #100).

.. _changes_0.4.2:

`v0.4.2 <https://github.com/bird-house/cookiecutter-birdhouse/tree/v0.4.2>`_  (2020-01-07)
------------------------------------------------------------------------------------------

Changes:

* Fix conda environment for latest cookiecutter (#75).
* Pinned PyWPS 4.2 (#74).
* Updated links to developer guide (#73).
* Added setuptools to conda environment (#72).

.. _changes_0.4.1:

`v0.4.1 <https://github.com/bird-house/cookiecutter-birdhouse/tree/v0.4.1>`_  (2019-09-27)
------------------------------------------------------------------------------------------

This is the Bucharest release.

Changes:

* Skipped conda environment handling in makefile (#70).

.. _changes_0.4.0:

`v0.4.0 <https://github.com/bird-house/cookiecutter-birdhouse/tree/v0.4.0>`_  (2019-04-17)
------------------------------------------------------------------------------------------

This is the San Francisco release.

Changes:

* Skipped python 2.7 support (#67).
* Updated to pywps 4.2 (#66).
* Added `make spec` (#65).
* Fixed Emu references (#63).

.. _changes_0.3.1:

`v0.3.1 <https://github.com/bird-house/cookiecutter-birdhouse/tree/v0.3.1>`_  (2018-12-05)
------------------------------------------------------------------------------------------

Bugfixes for Washington release.

Changes:

* Raise Makefile errors (#57).
* Get version number without importing package (#56).
* Keep only a single *hello* process (#53).

.. _changes_0.3.0:

`v0.3.0 <https://github.com/bird-house/cookiecutter-birdhouse/tree/v0.3.0>`_  (2018-09-05)
------------------------------------------------------------------------------------------

Cookiecutter template prepared for Ansible deployment of PyWPS.

Changes:

* Updated to Ansible deployment (#14).
* Enabled PyWPS autodoc extension (#37).
* Updated PyWPS CLI (#8 and #33).
* Enabled Conda support for RTD (#51).
* Using ``bumpversion`` to update version (#9)
* numerous fixes.

.. _changes_0.2.0:

`v0.2.0 <https://github.com/bird-house/cookiecutter-birdhouse/tree/v0.2.0>`_  (2018-05-22)
------------------------------------------------------------------------------------------

Initial Cookiecutter Birdhouse release.

A Cookiecutter template for a minimal PyWPS server with example processes.

.. _changes_0.1.1:

`v0.1.1 <https://github.com/bird-house/cookiecutter-birdhouse/tree/v0.1.1>`_  (2016-06-04)
------------------------------------------------------------------------------------------

Original Cookiecutter:
https://github.com/audreyr/cookiecutter-pypackage/tree/v0.1.1
