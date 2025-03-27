
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_post_ask():
    response = client.post("/api/ask", json={"query": "¿Qué es IA?"})
    assert response.status_code == 200
    assert "generated_text" in response.json()
