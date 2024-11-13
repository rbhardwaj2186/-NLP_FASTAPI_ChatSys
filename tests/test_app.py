# tests/test_app.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predefined_response():
    response = client.post("/query", json={"question": "Create an action plan", "client_id": 101})
    assert response.status_code == 200
    assert "Action Plan" in response.json()["response"]

def test_gpt_fallback():
    response = client.post("/query", json={"question": "Non-existing question", "client_id": 999})
    assert response.status_code == 200
    assert "GPT Response" in response.json()["response"]
