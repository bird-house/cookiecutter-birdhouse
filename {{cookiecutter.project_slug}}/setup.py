#!/usr/bin/env python

"""The setup script."""

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
REQUIRES_PYTHON = ">=3.6.0"

about = {}
with open(os.path.join(here, '{{ cookiecutter.project_slug }}', '__version__.py'), 'r') as f:
    exec(f.read(), about)

{%- if cookiecutter.use_pytest == 'n' %}

test_requirements = [{%- if cookiecutter.use_pytest == 'y' %}'pytest>=3',{%- endif %} ]

{%- endif %}

requirements = [line.strip() for line in open('requirements.txt')]

dev_reqs = [line.strip() for line in open('requirements_dev.txt')]

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}


classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Natural Language :: English',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Topic :: Scientific/Engineering :: Atmospheric Science',
{%- if cookiecutter.open_source_license in license_classifiers %}
    '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
]

setup(
    name='{{ cookiecutter.project_slug }}',
    version=about['__version__'],
    description="{{ cookiecutter.project_short_description }}",
    long_description=README + '\n\n' + CHANGES,
    long_description_content_type="text/x-rst",
    author=about['__author__'],
    author_email=about['__email__'],
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_repo_name }}',
    python_requires=REQUIRES_PYTHON,
    classifiers=classifiers,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    zip_safe=False,
    keywords='wps pywps birdhouse {{ cookiecutter.project_slug }}',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
{%- if cookiecutter.use_pytest == 'n' %}
    test_suite='tests',
    tests_require=test_requirements,
{%- endif %}
    extras_require={
        "dev": dev_reqs,  # pip install ".[dev]"
    },
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:cli',
        ]
    }
)
