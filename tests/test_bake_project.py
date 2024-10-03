from contextlib import contextmanager
import shlex
import os
import sys
from pathlib import Path
import subprocess
import datetime
import pytest
from cookiecutter.utils import rmtree


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    kwargs.update(template=Path(__file__).parents[1].as_posix())
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project_path))


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def check_output_inside_dir(command, dirpath):
    "Run a command from inside a given directory, returning the command output"
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))


def test_year_compute_in_license_file(cookies):
    with bake_in_temp_dir(cookies) as result:
        license_file_path = result.project_path.joinpath("LICENSE")
        now = datetime.datetime.now()
        assert str(now.year) in license_file_path.read_text()


def project_info(result):
    """Get toplevel dir, project_slug, and project dir from baked cookies"""
    assert result.exception is None
    assert result.project_path.isdir()

    project_path = result.project_path
    project_slug = os.path.split(project_path)[-1]
    project_dir = os.path.join(project_path, project_slug)
    return project_path, project_slug, project_dir


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project_path.is_dir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.name for f in result.project_path.iterdir()]
        assert "LICENSE" in found_toplevel_files
        assert "Makefile" in found_toplevel_files
        assert "README.rst" in found_toplevel_files
        assert "environment.yml" in found_toplevel_files
        assert "environment-dev.yml" in found_toplevel_files
        assert "environment-docs.yml" in found_toplevel_files
        assert 'pyproject.toml' in found_toplevel_files
        assert 'tox.ini' in found_toplevel_files
        assert 'tests' in found_toplevel_files
        assert "src" in found_toplevel_files
        assert (
            "babybird"
            in next(result.project_path.joinpath("src").iterdir()).name
        )
        assert "tox.ini" in found_toplevel_files

@pytest.mark.requires_gdal
def test_bake_and_run_tests(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project_path.is_dir()
        assert run_inside_dir('which python', str(result.project_path)) == 0
        assert run_inside_dir('pip install -e .', str(result.project_path)) == 0
        assert run_inside_dir('pytest tests', str(result.project_path)) == 0
        print("test_bake_and_run_tests path", str(result.project_path))


@pytest.mark.precommit
def test_bake_and_run_pre_commit(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project_path.is_dir()
        assert run_inside_dir("git init", str(result.project_path)) == 0
        assert run_inside_dir("git add *", str(result.project_path)) == 0
        assert run_inside_dir("pre-commit install", str(result.project_path)) == 0
        assert (
            run_inside_dir(
                "pre-commit run --all-files --show-diff-on-failure",
                str(result.project_path),
            )
            == 0
        )
        print("test_bake_and_run_pre_commit path", str(result.project_path))

def test_bake_and_build_package(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project_path.is_dir()
        assert run_inside_dir("python -m flit build", str(result.project_path)) == 0
        assert run_inside_dir("twine check dist/*", str(result.project_path)) == 0
        print("test_bake_and_build_package path", str(result.project_path))


@pytest.mark.requires_gdal
def test_bake_with_special_chars_and_run_tests(cookies):
    """Ensure that a `full_name` with double quotes does not break pyproject.toml."""
    with bake_in_temp_dir(
        cookies, extra_context={"full_name": 'name "quote" name', "use_pytest": "n"}
    ) as result:
        assert result.project_path.is_dir()
        assert run_inside_dir("python -m coverage", str(result.project_path)) == 0


@pytest.mark.requires_gdal
def test_bake_with_apostrophe_and_run_tests(cookies):
    """Ensure that a `full_name` with apostrophes does not break pyproject.toml."""
    with bake_in_temp_dir(
        cookies, extra_context={"full_name": "O'connor", "use_pytest": "n"}
    ) as result:
        assert result.project_path.is_dir()
        assert run_inside_dir("python -m coverage", str(result.project_path)) == 0


def test_bake_without_author_file(cookies):
    with bake_in_temp_dir(
        cookies,
        extra_context={'create_author_file': 'n'}
    ) as result:
        found_toplevel_files = [f.name for f in result.project_path.iterdir()]
        assert 'AUTHORS.rst' not in found_toplevel_files
        doc_files = [f.name for f in result.project_path.joinpath('docs').joinpath('source').iterdir()]
        assert 'authors.rst' not in doc_files

        # Assert there are no spaces in the toc tree
        docs_index_path = result.project_path.joinpath('docs/source/index.rst')
        with open(str(docs_index_path)) as index_file:
            assert 'installation\n   configuration\n   notebooks/index\n   dev_guide' \
                   '\n   processes\n   changes\n' in index_file.read()

        pyproject_path = result.project_path.joinpath("pyproject.toml")
        with open(str(pyproject_path)) as pyproject_file:
            assert 'AUTHORS.rst' not in pyproject_file.read()



def test_make_help(cookies):
    with bake_in_temp_dir(cookies) as result:
        # The supplied Makefile does not support win32
        if sys.platform != "win32":
            output = check_output_inside_dir(
                'make help',
                str(result.project_path)
            )
            assert b"Please use 'make <target>' where <target> is one of:" in output


def test_bake_selecting_license(cookies):
    license_strings = {
        "MIT license": ("MIT", "License :: OSI Approved :: MIT License"),
        "BSD license": (
            "Redistributions of source code must retain the above copyright notice, this",
            "License :: OSI Approved :: BSD License",
        ),
        "ISC license": ("ISC License", "License :: OSI Approved :: ISC License"),
        "Apache Software License 2.0": (
            "Licensed under the Apache License, Version 2.0",
            "License :: OSI Approved :: Apache Software License",
        ),
        "GNU General Public License v3": (
            "GNU GENERAL PUBLIC LICENSE",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        ),
    }
    for license_code, target_strings in license_strings.items():
        with bake_in_temp_dir(
            cookies, extra_context={"open_source_license": license_code}
        ) as result:
            assert (
                target_strings[0] in result.project_path.joinpath("LICENSE").read_text()
            )
            assert (
                target_strings[1]
                in result.project_path.joinpath("pyproject.toml").read_text()
            )



def test_bake_not_open_source(cookies):
    with bake_in_temp_dir(
        cookies,
        extra_context={'open_source_license': 'Not open source'}
    ) as result:
        found_toplevel_files = [f.name for f in result.project_path.iterdir()]
        assert 'pyproject.toml' in found_toplevel_files
        assert 'LICENSE' not in found_toplevel_files
        assert 'License' not in result.project_path.joinpath('README.rst').read_text()


@pytest.mark.parametrize("use_black,expected", [("y", True), ("n", False)])
def test_black(cookies, use_black, expected):
    with bake_in_temp_dir(cookies, extra_context={"use_black": use_black}) as result:
        assert result.project_path.is_dir()
        requirements_path = result.project_path.joinpath("pyproject.toml")
        assert ("black ==" in requirements_path.read_text()) is expected
        assert ("isort ==" in requirements_path.read_text()) is expected
        assert ("[tool.black]" in requirements_path.read_text()) is expected
        makefile_path = result.project_path.joinpath("Makefile")
        assert ("black --check" in makefile_path.read_text()) is expected
