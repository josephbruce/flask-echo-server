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
    response = client.post('/strlen', json={"text": "Hello, World!"})
    assert response.status_code == 200
    assert response.get_json() == {"length": 13}

def test_strlen_invalid_json(client):
    response = client.post('/strlen', data="not json", content_type='application/json')
    assert response.status_code == 400

def test_strlen_missing_content_type(client):
    response = client.post('/strlen', data="something")
    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid JSON"}

def test_strlen_non_string(client):
    response = client.post('/strlen', json={"text": 123})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Text must be a string"}

def test_strlen_json_list(client):
    response = client.post('/strlen', json=["not", "dict"])
    assert response.status_code == 400
    assert response.get_json() == {"error": "JSON body must be a dictionary"}

def test_strlen_missing_field(client):
    response = client.post('/strlen', json={})
    assert response.status_code == 400
    assert response.get_json() == {"error": "'text' field is required"}
