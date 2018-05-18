==========================
Cookiecutter for Birdhouse
==========================

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


Cookiecutter_ template for a Birdhouse bird package (pyWPS server).

* GitHub repo: https://github.com/birdhouse/cookiecutter-birdhouse/
* Documentation: https://birdhouse.readthedocs.io/
* Free software: BSD license

Features
--------

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

Prior to installing cookiecutter-birdhouse, the cookiecutter package must be installed in your environment.
This is achieved via the following command::

    $ conda install -c conda-forge cookiecutter

With cookiecutter installed, the cookiecutter-birdhouse template can be installed with::

    $ cookiecutter https://github.com/bird-house/cookiecutter-birdhouse.git

Once cookiecutter clones the template, you will be asked a series of questions related to your project::
.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter

    $ full_name [Full Name]: Enter your full name.

    $ email [Email Address]: Enter your email address.

    $ github_username [bird-house]: Accept the default or enter your github username.

    $ project_name [Babybird]: The name of your new bird.

    $ project_slug [babybird]: The name of your bird used as Python package.

    $ project_short_description [Short description]: Enter a short description about your project.

    $ version [0.1.0]: Enter the version number for your application.

    $ http_port [5000]: The HTTP port on which your service will be accessible.

    $ https_port [25000]: The HTTPS port on which your service will be accessible.

    $ output_port [8090]: The HTTP port on which your service outputs will be accessible.

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

Development
-----------

If you want to extend the cookiecutter template then prepare your development
environment as follows::

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


.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-pypackage tutorial`: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html
.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _Read the Docs: https://readthedocs.io/
.. _`pyup.io`: https://pyup.io/
.. _bump2version: https://github.com/c4urself/bump2version
.. _Punch: https://github.com/lgiordani/punch
.. _Poetry: https://python-poetry.org/
.. _PyPi: https://pypi.python.org/pypi

