"""Unimplemented Milestone 1+ endpoints must say so explicitly (HTTP 501),
never fabricate a success response (master prompt Section 5)."""

import pytest
from fastapi.testclient import TestClient

UNIMPLEMENTED_ENDPOINTS = [
    ("post", "/api/v1/auth/register"),
    ("post", "/api/v1/auth/login"),
    ("get", "/api/v1/profiles/me"),
    ("post", "/api/v1/meal-plans/generate"),
    ("get", "/api/v1/grocery-lists/current"),
    ("post", "/api/v1/feedback/recipes/1"),
    ("get", "/api/v1/dashboard/summary"),
    ("get", "/api/v1/admin/foods"),
    ("get", "/api/v1/admin/recipes"),
    ("get", "/api/v1/admin/nutrition"),
    ("get", "/api/v1/admin/categories"),
]


@pytest.mark.parametrize("method,path", UNIMPLEMENTED_ENDPOINTS)
def test_unimplemented_endpoint_returns_501(
    client: TestClient, method: str, path: str
) -> None:
    response = getattr(client, method)(path)
    assert response.status_code == 501
    assert "not implemented" in response.json()["error"].lower()
