{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg
        :target: https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status
{%- endif %}

.. image:: https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.project_repo_name }}.svg
    :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_repo_name }}/blob/master/LICENSE.txt
    :alt: GitHub license

.. image:: https://badges.gitter.im/bird-house/birdhouse.svg
    :target: https://gitter.im/bird-house/birdhouse?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
    :alt: Join the chat at https://gitter.im/bird-house/birdhouse

{{ cookiecutter.project_name }} (the bird)
  *{{ cookiecutter.project_name }} is a bird ...*

{{ cookiecutter.project_short_description }}

Documentation
-------------

Learn more about {{ cookiecutter.project_name }} in its official documentation at
https://{{ cookiecutter.project_readthedocs_name }}.readthedocs.io.

Submit bug reports, questions and feature requests at
https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_repo_name }}/issues

Contributing
------------

You can find information about contributing in our `Developer Guide`_.

Please use bumpversion_ to release a new version.

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
.. _bumpversion: https://{{ cookiecutter.project_readthedocs_name }}.readthedocs.io/en/latest/dev_guide.html#bump-a-new-version
