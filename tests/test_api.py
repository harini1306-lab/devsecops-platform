from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "DevSecOps Backend Running"


def test_pipeline_status():
    response = client.get("/api/status")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_latest_commit():
    response = client.get("/api/commit")
    assert response.status_code == 200
    data = response.json()
    assert "commit" in data
    assert "author" in data
    assert "branch" in data
