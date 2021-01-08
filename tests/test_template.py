import pytest


@pytest.fixture
def context():
    """Test template creation with test parameters."""
    return {
        "full_name": "test name",
        "email": "test@email.com",
        "github_username": "test_username",
        "project_name": "Test Bird",
        "pypi_username": "test_name",
        "project_slug": "testbird",
        "project_repo_name": "testbird",
        "project_readthedocs_name": "testbird",
        "project_short_description": "Test description.",
        "version": "0.1.0",
        "open_source_license": "MIT license",
        "permanent_address": "https://pavics.ouranos.ca",
        "use_pytest": "y",
        "use_pypi_deployment_with_travis": "y",
        "add_pyup_badge": "n",
        "command_line_interface": ["Click", "Argparse", "No command-line interface"],
        "create_author_file": "y",
        "_copy_without_render": "testbird/templates/*.cfg"
    }


def test_template(cookies, context):
    """Test the template for proper creation.

    cookies is a fixture provided by the pytest-cookies
    plugin. Its bake() method creates a temporary directory
    and installs the cookiecutter template into that directory.
    """
    result = cookies.bake(extra_context=context)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'testbird'
    assert result.project.isdir()
