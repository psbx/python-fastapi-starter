from fastapi.testclient import TestClient
from app import app
client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200 and r.json()["ok"] is True

def test_echo():
    r = client.post("/echo", json={"text": "hey"})
    assert r.json()["echo"] == "hey"
