{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %}
+----------------------------+-----------------------------------------------------+
| Versions                   | |pypi| |conda| |versions|                           |
{%- endif %}
+----------------------------+-----------------------------------------------------+
| Documentation and Support  | |docs| |gitter|                                     |
{%- if is_open_source %}
+----------------------------+-----------------------------------------------------+
| Open Source                | |license|                                           |
{%- endif %}
{%- if cookiecutter.use_black == 'y' %}
+----------------------------+-----------------------------------------------------+
| Coding Standards           | |black| |isort| |pre-commit| |ruff|                 |
{%- else %}
+----------------------------+-----------------------------------------------------+
| Coding Standards           | |pre-commit| |ruff|                                 |
{%- endif %}
+----------------------------+-----------------------------------------------------+
| Development Status         | |status| |build|                                    |
+----------------------------+-----------------------------------------------------+

{{ cookiecutter.project_name }} (the bird)
  *{{ cookiecutter.project_name }} is a bird ...*

{{ cookiecutter.project_short_description }}

Documentation
-------------

Learn more about {{ cookiecutter.project_name }} in its official documentation at https://{{ cookiecutter.project_readthedocs_name }}.readthedocs.io.

Submit bug reports, questions and feature requests at https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_repo_name }}/issues

Contributing
------------

You can find information about contributing in our `Developer Guide`_.

Please use bump-my-version_ to release a new version.

{% if is_open_source %}
License
-------

* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}

Credits
-------

This package was created with Cookiecutter_ and the `bird-house/cookiecutter-birdhouse`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`bird-house/cookiecutter-birdhouse`: https://github.com/bird-house/cookiecutter-birdhouse
.. _`Developer Guide`: https://{{ cookiecutter.project_readthedocs_name }}.readthedocs.io/en/latest/dev_guide.html
.. _bump-my-version: https://{{ cookiecutter.project_readthedocs_name }}.readthedocs.io/en/latest/dev_guide.html#bump-a-new-version

{% if cookiecutter.use_black == 'y' -%}
.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :target: https://github.com/psf/black
        :alt: Python Black

{% endif -%}
.. |build| image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/main.yml/badge.svg
        :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/main.yml
        :alt: Build Status

.. |conda| image:: https://img.shields.io/conda/vn/conda-forge/{{ cookiecutter.project_slug }}.svg
        :target: https://anaconda.org/conda-forge/{{ cookiecutter.project_slug }}
        :alt: Conda-forge Build Version

.. |docs| image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status

.. |gitter| image:: https://badges.gitter.im/bird-house/birdhouse.svg
        :target: https://gitter.im/bird-house/birdhouse
        :alt: Bird-house Gitter Chat

{%- if cookiecutter.use_black == 'y' %}

.. |isort| image:: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
        :target: https://pycqa.github.io/isort/
        :alt: Isort
{%- endif -%}

{%- if is_open_source %}

.. |license| image:: https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.project_repo_name }}.svg
        :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_repo_name }}/blob/main/LICENSE.txt
        :alt: License

.. |pypi| image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}
        :alt: Python Package Index Build
{%- endif %}

.. |pre-commit| image:: https://results.pre-commit.ci/badge/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_repo_name }}/main.svg
        :target: https://results.pre-commit.ci/latest/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_repo_name }}/main
        :alt: pre-commit.ci status

.. |ruff| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
        :target: https://github.com/astral-sh/ruff
        :alt: Ruff

.. |status| image:: https://www.repostatus.org/badges/latest/wip.svg
        :alt: Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.
        :target: https://www.repostatus.org/#wip

.. |versions| image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}
        :alt: Supported Python Versions
