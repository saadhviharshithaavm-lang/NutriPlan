"""Smoke tests: the application module imports and builds without error."""

from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.main import app


def test_app_is_fastapi_instance() -> None:
    assert isinstance(app, FastAPI)


def test_app_has_health_route() -> None:
    client = TestClient(app)
    response = client.get("/api/v1/health")
    assert response.status_code == 200


def test_docs_available() -> None:
    assert app.docs_url == "/docs"
