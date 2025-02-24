from fastapi.testclient import TestClient
import urllib.parse
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_root_custom_message():
    query_params = {"message": "Dlrow olleH"}
    response = client.get("/?" + urllib.parse.urlencode(query_params))
    assert response.status_code == 200
    assert response.json() == {"message": "Dlrow olleH"}
