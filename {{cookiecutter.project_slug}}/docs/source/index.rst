.. include:: ../../README.rst

.. toctree::
   :maxdepth: 1
   :caption: Table of Contents

   installation
   configuration
   notebooks/index
   dev_guide
   processes
   {%- if cookiecutter.create_author_file == 'y' %}
   authors
   {%- endif %}
   changelog

.. toctree::
   :maxdepth: 2
   :caption: Package Structure

   apidoc/modules

.. toctree::
   :caption: GitHub Repository

   {{ cookiecutter.github_username }}/{{ cookiecutter.project_name.replace(' ', '-') }} <{{ cookiecutter.__gh_slug }}>

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
