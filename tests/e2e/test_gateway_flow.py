from pathlib import Path
import sys

from fastapi.testclient import TestClient

sys.path.append(str(Path(__file__).resolve().parents[2]))

from services.gateway.app.main import app


client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["service"] == "gateway"


def test_create_and_fetch_vault() -> None:
    create_response = client.post(
        "/vaults",
        json={"owner_name": "Jane Doe", "parcel_id": "parcel-001"},
    )
    assert create_response.status_code == 201
    created = create_response.json()

    get_response = client.get(f"/vaults/{created['id']}")
    assert get_response.status_code == 200
    fetched = get_response.json()

    assert fetched["id"] == created["id"]
    assert fetched["owner_name"] == "Jane Doe"
