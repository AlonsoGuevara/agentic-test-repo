import pytest
from fastapi.testclient import TestClient

from agentic_test_repo.app import create_app


@pytest.fixture
def client():
    return TestClient(create_app())


def test_health_returns_200(client) -> None:
    response = client.get("/health")
    assert response.status_code == 200


def test_health_returns_ok_status(client) -> None:
    response = client.get("/health")
    assert response.json() == {"status": "ok"}


def test_health_response_schema(client) -> None:
    """Response should match the HealthResponse Pydantic model schema."""
    response = client.get("/health")
    data = response.json()
    assert "status" in data
    assert isinstance(data["status"], str)
