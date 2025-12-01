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
    response = client.post('/strlen', json={"message": "Hello"})
    assert response.status_code == 200
    assert response.get_json() == {"length": 5}

def test_strlen_empty_body(client):
    response = client.post('/strlen', data=b'', content_type='application/json')
    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid or empty JSON body"}

def test_strlen_non_string_message(client):
    response = client.post('/strlen', json={"message": 123})
    assert response.status_code == 400
    assert response.get_json() == {"error": "'message' must be a string"}
