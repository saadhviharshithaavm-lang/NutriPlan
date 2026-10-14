from fastapi.testclient import TestClient


def test_health_endpoint_returns_ok(client: TestClient) -> None:
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["app_name"] == "NutriPlan API"


def test_health_endpoint_has_swagger_docs(client: TestClient) -> None:
    response = client.get("/docs")
    assert response.status_code == 200
