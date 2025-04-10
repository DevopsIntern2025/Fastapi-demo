"""Test module for FastAPI root endpoint."""

from fastapi.testclient import TestClient
from fastapi_pr_demo.main import app

client = TestClient(app)

def test_read_root():
    """Test for GET /"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World, from FastAPI"}
