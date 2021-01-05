==========================
Cookiecutter for Birdhouse
==========================

.. image:: https://img.shields.io/badge/docs-latest-brightgreen.svg
   :target: http://cookiecutter-birdhouse.readthedocs.org/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://travis-ci.org/bird-house/cookiecutter-birdhouse.svg?branch=master
   :target: https://travis-ci.org/bird-house/cookiecutter-birdhouse
   :alt: Travis Build

.. image:: https://img.shields.io/github/license/bird-house/cookiecutter-birdhouse.svg
    :target: https://github.com/bird-house/cookiecutter-birdhouse/blob/master/LICENSE
    :alt: GitHub license

.. image:: https://badges.gitter.im/bird-house/birdhouse.svg
    :target: https://gitter.im/bird-house/birdhouse?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
    :alt: Join the chat at https://gitter.im/bird-house/birdhouse

.. image:: https://pyup.io/repos/github/audreyr/cookiecutter-pypackage/shield.svg
    :target: https://pyup.io/repos/github/audreyr/cookiecutter-pypackage/
    :alt: Updates

*A Cookiecutter template for a Birdhouse bird package*

Cookiecutter_ is a command-line utility to create projects from templates. This `cookiecutter-birdhouse`
template creates a barebone PyWPS server adhering to Birdhouse conventions. It comes complete with a
framework for installation, configuration, deployment, documentation and tests. It even includes a
:file:`Dockerfile` for containerization! Create your project then get started writing new WPS
processes in minutes.

To keep projects up-to-date with the cookiecutter template, Cruft_ will be
used.

* GitHub repo: https://github.com/bird-house/cookiecutter-birdhouse/
* Documentation: https://cookiecutter-birdhouse.readthedocs.io/en/latest/
* Free software: BSD license


.. warning::

   This is the cookiecutter template for PyWPS *without* the Buildout deployment.
   The template for the Buildout deployment is on branch `0.2.x`_.

Features
--------

* Ready-made PyWPS server (a bird)
* Pre-configured :file:`.travis.yml` for Travis-CI_ automated deployment and testing
* Pre-configured :file:`.codacy.yml` for automated Codacy_ code review
* A :file:`Dockerfile` and :file:`docker-compose.yml` for containerization
* Preconfigured Sphinx_ documentation that can be hosted on ReadTheDocs_
* A :file:`Makefile` to install the code, start, stop and poll the server and more
* Testing setup with ``unittest`` and ``python setup.py test`` or ``pytest``
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 3.5, 3.6, 3.7, 3.8
* Sphinx_ docs: Documentation ready for generation with, for example, `Read the Docs`_
* bump2version_: Pre-configured version bumping with a single command
* Auto-release to PyPI_ when you push a new tag to master (optional)
* Command line interface using Click (optional)

Build Status
-------------

Linux:

.. image:: https://img.shields.io/travis/audreyfeldroy/cookiecutter-pypackage.svg
    :target: https://travis-ci.org/audreyfeldroy/cookiecutter-pypackage
    :alt: Linux build status on Travis CI

Installation
------------

Prior to installing cookiecutter-birdhouse, the cookiecutter and cruft package must be installed in your environment.
This is achieved via the following commands:

.. code-block:: console

    $ conda install -c conda-forge cookiecutter
    $ pip install cruft

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
    Choose from 1, 2, 3, 4, 5 [1]: 
    http_port [5000]: 

The answer to all those questions are recorded in the ``.cruft.json`` file in
your generated bird.

Usage
-----

After answering the questions asked during installation, a *bird* Python package will be
created in your current working directory. This package will contain a configurable PyWPS
service with some initial test processes.

Then:

* Create a repo and put it there.
* Add the repo to your Travis-CI_ account.
* Install the dev requirements into a virtualenv. (``pip install -r requirements_dev.txt``)
* Register_ your project with PyPI.
* Run the Travis CLI command ``travis encrypt --add deploy.password`` to encrypt your PyPI password in Travis config
  and activate automated deployment on PyPI when you push a new tag to master branch.
* Add the repo to your `Read the Docs`_ account + turn on the Read the Docs service hook.
* Release your package by pushing a new tag to master.
* Add a ``requirements.txt`` file that specifies the packages you will need for
  your project and their versions. For more info see the `pip docs for requirements files`_.
* Activate your project on `pyup.io`_.

.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files
.. _Register: https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives

For more details, see the `cookiecutter-pypackage tutorial`_.

See the `babybird <http://babybird.rtfd.io/>`_ example of a generated bird.

To keep the generated bird up-to-date with the cookiecutter template:

.. code-block:: console

    $ cruft update  # uses configurations in the .cruft.json file

Cruft can be configured to ignore template change to certain files, see
https://timothycrosley.github.io/cruft/#updating-a-project.  Potential files to
ignore:

* initial example files because we do not want to keep those
* environment files and list of processes, list of tutorial notebooks since they
  natually are different between each bird

See cruft_skip_ example.

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
  * Dry Run: ``bumpversion --dry-run --verbose --new-version 0.3.1 patch``
  * Do it: ``bumpversion --new-version 0.3.1 patch``
  * ... or: ``bumpversion --new-version 0.4.0 minor``
  * Push it: ``git push --tags``

See the bumpversion_ documentation for details.


.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Cruft: https://timothycrosley.github.io/cruft/
.. _`cookiecutter-pypackage tutorial`: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html
.. _cruft_skip: https://github.com/Ouranosinc/raven/blob/4d32f82cc993e5569eb7afc86aefd7ed88824b78/.cruft.json#L4-L14
.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Codacy: http://codacy.com
.. _Sphinx: http://sphinx-doc.org/
.. _Read the Docs: https://readthedocs.io/
.. _`pyup.io`: https://pyup.io/
.. _bump2version: https://github.com/c4urself/bump2version
.. _Punch: https://github.com/lgiordani/punch
.. _Poetry: https://python-poetry.org/
.. _PyPi: https://pypi.python.org/pypi
.. _0.2.x: https://github.com/bird-house/cookiecutter-birdhouse/tree/0.2.x
