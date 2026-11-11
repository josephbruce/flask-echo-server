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

def test_strlen_text(client):
    response = client.post('/strlen', json={"text": "Hello, World!"})
    assert response.status_code == 200
    assert response.get_json() == {"length": 13}

def test_strlen_empty_string(client):
    response = client.post('/strlen', json={"text": ""})
    assert response.status_code == 200
    assert response.get_json() == {"length": 0}

def test_strlen_string_key(client):
    response = client.post('/strlen', json={"string": "foobar"})
    assert response.status_code == 200
    assert response.get_json() == {"length": 6}

def test_strlen_missing_field(client):
    response = client.post('/strlen', json={"other": "foobar"})
    assert response.status_code == 400
    assert "error" in response.get_json()

def test_strlen_invalid_type(client):
    response = client.post('/strlen', json={"text": 12345})
    assert response.status_code == 400
    assert "error" in response.get_json()

def test_strlen_non_json(client):
    response = client.post('/strlen', data="raw string")
    assert response.status_code == 400
    assert "error" in response.get_json()
