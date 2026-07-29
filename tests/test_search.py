from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_search():

    response = client.post(
        "/api/v1/search",
        json={
            "query": "Claims API"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "summary" in data