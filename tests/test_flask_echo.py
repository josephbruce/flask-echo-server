import pytest
from flask_echo_server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_echo(client):
    response = client.post('/echo', json={"message": "Hello, World!"})
    assert response.status_code == 200
    assert response.get_json() == {"echo": {"message": "Hello, World!"}}

def test_strlen(client):
    response = client.post('/strlen', json={"text": "some string"})
    assert response.status_code == 200
    assert response.get_json() == {"length": 11}

def test_strlen_invalid_json(client):
    response = client.post('/strlen', data="not json", content_type='application/json')
    assert response.status_code == 400
    assert "error" in response.get_json()

def test_strlen_not_dict(client):
    response = client.post('/strlen', json=["not a dict"])
    assert response.status_code == 400
    assert "error" in response.get_json()

def test_strlen_not_string(client):
    response = client.post('/strlen', json={"text": 123})
    assert response.status_code == 400
    assert "error" in response.get_json()
