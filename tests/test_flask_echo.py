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
    response = client.post('/strlen', json={"message": "Hello, World!"})
    assert response.status_code == 200
    assert response.get_json() == {"length": 13}

def test_strlen_empty(client):
    response = client.post('/strlen', json={"message": ""})
    assert response.status_code == 200
    assert response.get_json() == {"length": 0}

def test_strlen_non_ascii(client):
    response = client.post('/strlen', json={"message": "你好"})
    assert response.status_code == 200
    assert response.get_json() == {"length": 6}

def test_strlen_invalid_json(client):
    response = client.post('/strlen', data="not json", content_type='application/json')
    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid JSON or missing \"message\" key"}

def test_strlen_missing_message_key(client):
    response = client.post('/strlen', json={"msg": "Hello"})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid JSON or missing \"message\" key"}

def test_strlen_message_not_a_string(client):
    response = client.post('/strlen', json={"message": 123})
    assert response.status_code == 400
    assert response.get_json() == {"error": "\"message\" must be a string"}
