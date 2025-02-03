==========================
Cookiecutter for Birdhouse
==========================

.. image:: https://img.shields.io/badge/docs-latest-brightgreen.svg
   :target: http://cookiecutter-birdhouse.readthedocs.org/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://github.com/bird-house/cookiecutter-birdhouse/actions/workflows/main.yml/badge.svg
   :target: https://github.com/bird-house/cookiecutter-birdhouse/actions/workflows/main.yml
   :alt: GitHub Workflows

.. image:: https://readthedocs.org/projects/cookiecutter-pypackage/badge/?version=latest
   :target: https://cookiecutter-pypackage.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://img.shields.io/github/license/bird-house/cookiecutter-birdhouse.svg
   :target: https://github.com/bird-house/cookiecutter-birdhouse/blob/master/LICENSE
   :alt: GitHub license

.. image:: https://badges.gitter.im/bird-house/birdhouse.svg
   :target: https://gitter.im/bird-house/birdhouse?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
   :alt: Join the chat at https://gitter.im/bird-house/birdhouse

Cookiecutter_ template for a Python package.

*A Cookiecutter template for a Birdhouse bird package*

Cookiecutter_ is a command-line utility to create projects from templates. This `cookiecutter-birdhouse` template creates a barebones PyWPS server adhering to Birdhouse conventions.
It comes complete with a framework for installation, configuration, deployment, documentation and tests.
It even includes a `Dockerfile` for containerization!
Create your project then get started writing new WPS processes in minutes.

You may at any time update your project using the latest cookiecutter template using Cruft_.

* GitHub repo: https://github.com/bird-house/cookiecutter-birdhouse/
* Documentation: http://cookiecutter-birdhouse.readthedocs.io/en/latest/
* Free software: BSD license
* Discord: https://discord.gg/PWXJr3upUE

.. warning::

   This is the cookiecutter template for PyWPS *without* the Buildout deployment.
   The template for the Buildout deployment is on branch `0.2.x`_.

Features
--------

* Testing setup with ``pytest`` and ``tox``
* GitHub_Workflows_: Ready for GitHub Workflows Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 3.9, 3.10, 3.11, and 3.12
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_
* bump-my-version_: Pre-configured version bumping with a single command
* Auto-release to PyPI_ when you push a new tag to master (optional)
* A `Makefile` to install the code, start, stop, poll the server and more

Installation
------------

Prior to installing cookiecutter-birdhouse, the `cookiecutter` and `cruft` packages must be installed in your environment.
This is achieved via the following commands:

.. code-block:: console

    $ python -m pip install cookiecutter
    $ python -m pip install cruft

With cookiecutter and cruft installed, the cookiecutter-birdhouse template can be installed with:

.. code-block:: console

    $ cruft create https://github.com/bird-house/cookiecutter-birdhouse.git

Once cookiecutter clones the template, you will be asked a series of questions related to your project:

.. code-block:: console

    full_name [Full Name]:
    email [your@email]:
    github_username [bird-house]:
    project_name [Babybird]:
    project_slug [babybird]:
    project_repo_name [babybird]:
    project_readthedocs_name [babybird]:
    project_short_description [A Web Processing Service for Climate Data Analysis.]:
    version [0.1.0]:
    Select open_source_license:
    1 - Apache Software License 2.0
    2 - MIT license
    3 - BSD license
    4 - ISC license
    5 - GNU General Public License v3
    6 - Not open source
    Choose from 1, 2, 3, 4, 5, 6 [1]:
    http_port [5000]:
    use_pytest [y]:
    use_black [y]:
    create_author_file [y]:

The answer to all those questions are recorded in the ``.cruft.json`` file in
your generated bird.

Usage
-----

After answering the questions asked during installation, a *bird* Python package will be created in your current working directory.
This package will contain a configurable PyWPS service with some initial test processes.

Then:

* Create a repository on GitHub and upload files there.
* Enable GitHub_Workflows_ for the repository.
* Add the repo to your ReadTheDocs_ account, then turn on the ReadTheDocs service hook.

For more details, see the `cookiecutter-pypackage tutorial`_.

See the `babybird <http://babybird.rtfd.io/>`_ example of a generated bird.

To keep the generated bird up-to-date with the cookiecutter template:

.. code-block:: console

    $ cruft update  # uses configurations in the .cruft.json file

Cruft can be configured to ignore template changes to certain files, see
https://cruft.github.io/cruft/#updating-a-project.
Potential files to ignore:

* demonstration files, because they are meant to be erased
* environment files and list of processes, list of tutorial notebooks since they naturally are different between each bird

See cruft_skip_ example.

To link already generated project that was not initially generated using
``cruft create``:

.. code-block:: console

    $ cruft link https://github.com/bird-house/cookiecutter-birdhouse

This will create the ``.cruft.json`` file so subsequently ``cruft update`` can
be used.  You will need to answer the same questions as ``cruft create``
above.

.. note::

    After ``cruft link``, the ``commit`` field in the ``.cruft.json`` file will initially be wrong if you selected the default value.
    To ensure a proper subsequent ``cruft update``, you need to edit the ``.cruft.json`` file and put the proper last commit of the cookiecutter used in that ``commit`` field.
    See cruft_link_ example.

Development
-----------

If you want to extend the cookiecutter template then prepare your development
environment as follows:

.. code-block:: console

  # clone repo
  $ git clone git@github.com:bird-house/cookiecutter-birdhouse.git

  # change into repo
  $ cd cookiecutter-birdhouse

  # create conda environment
  $ conda env create -f environment.yml

  # activate conda environment
  $ source activate cookiecutter-birdhouse

  # run tests
  $ make test

  # bake a new bird with default settings
  $ make bake

  # the new "baked" bird is created in the cookies folder
  $ ls -l cookies/
  babybird

  # well ... you know what to do with a bird :)

  # finally you may clean it all up
  $ make clean

Bump a new version
------------------

Make a new version of this Cookiecutter in the following steps:

  * Make sure everything is commit to GitHub.
  * Update ``CHANGES.rst`` with the next version.
  * Dry Run: ``bump-my-version bump --dry-run --verbose --new-version 0.3.1 patch``
  * Do it: ``bump-my-version bump --new-version 0.3.1 patch``
  * ... or: ``bump-my-version bump --new-version 0.4.0 minor``
  * Push it: ``git push --tags``

See the bump-my-version_ documentation for details.

.. _0.2.x: https://github.com/bird-house/cookiecutter-birdhouse/tree/0.2.x
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Cruft: https://cruft.github.io/cruft/
.. _GitHub_Workflows: https://docs.github.com/en/actions/using-workflows
.. _Mkdocs: https://pypi.org/project/mkdocs/
.. _PyPI: https://pypi.python.org/pypi
.. _ReadTheDocs: https://readthedocs.io/
.. _Sphinx: http://sphinx-doc.org/
.. _Tox: http://testrun.org/tox/
.. _`cookiecutter-pypackage tutorial`: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html
.. _bump-my-version: https://github.com/callowayproject/bump-my-version
.. _cruft_link: https://github.com/bird-house/finch/pull/128/commits/0b0d7f37966cbb5bf345dfd4b4ac7953f38f4867
.. _cruft_skip: https://github.com/bird-house/emu/commit/fb1ff9ffdf9e7f0282b36ff0727996cba3bf081a
