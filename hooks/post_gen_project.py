#!/usr/bin/env python
from pathlib import Path

PROJECT_DIRECTORY = Path().cwd().absolute()

def remove_file(filepath):
    Path(PROJECT_DIRECTORY).joinpath(filepath).unlink()


if __name__ == "__main__":

    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_file("AUTHORS.rst")
        remove_file("docs/source//authors.rst")

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")
