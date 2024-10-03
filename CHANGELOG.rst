CHANGES
********

1.0.0 (2024-10-03)
==================

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

0.5.0 (2020-10-07)
==================

Changes:

* Easier to deploy new template to existing project using cruft (#85, #61).
* Use pip instead of setup.py (#97).
* Added conda forge, Python3.8, and osx build (#38).
* Backported fixes from birds (#86, #88, #89).
* Other fixes (#92, #93, #96, #100).

0.4.2 (2020-01-07)
==================

Changes:

* Fix conda environment for latest cookiecutter (#75).
* Pinned PyWPS 4.2 (#74).
* Updated links to developer guide (#73).
* Added setuptools to conda environment (#72).

0.4.1 (2019-09-27)
==================

This is the Bucharest release.

Changes:

* Skipped conda environment handling in makefile (#70).

0.4.0 (2019-04-17)
==================

This is the San Francisco release.

Changes:

* Skipped python 2.7 support (#67).
* Updated to pywps 4.2 (#66).
* Added `make spec` (#65).
* Fixed Emu references (#63).


0.3.1 (2018-12-05)
==================

Bugfixes for Washington release.

Changes:

* Raise Makefile errors (#57).
* Get version number without importing package (#56).
* Keep only a single *hello* process (#53).

0.3.0 (2018-09-05)
==================

Cookiecutter template prepared for Ansible deployment of PyWPS.

Changes:

* Updated to Ansible deployment (#14).
* Enabled PyWPS autodoc extension (#37).
* Updated PyWPS CLI (#8 and #33).
* Enabled Conda support for RTD (#51).
* Using ``bumpversion`` to update version (#9)
* numerous fixes.

0.2.0 (2018-05-22)
==================

Initial Cookiecutter Birdhouse release.

A Cookiecutter template for a minimal PyWPS server with example processes.

0.1.1 (2016-06-04)
==================

Original Cookiecutter:
https://github.com/audreyr/cookiecutter-pypackage/tree/v0.1.1
