from importlib.metadata import version

from fastapi.testclient import TestClient

from agentic_test_repo.app import create_app


def test_create_app_version_matches_package_metadata() -> None:
    """App version should match the installed package metadata."""
    app = create_app()
    assert app.version == version("agentic-test-repo")


def test_create_app_title() -> None:
    app = create_app()
    assert app.title == "Agentic Test Repo API"
