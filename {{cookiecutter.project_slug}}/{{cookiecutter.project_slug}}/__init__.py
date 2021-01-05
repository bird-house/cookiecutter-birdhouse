"""Top-level package for {{ cookiecutter.project_name }}."""

from .wsgi import application
from .cli import main

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'
