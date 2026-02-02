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
    # Test valid string
    response = client.post('/strlen', json={"text": "hello"})
    assert response.status_code == 200
    assert response.get_json() == {"length": 5}

    # Test empty string
    response = client.post('/strlen', json={"text": ""})
    assert response.status_code == 200
    assert response.get_json() == {"length": 0}

    # Test missing 'text' key
    response = client.post('/strlen', json={})
    assert response.status_code == 400
    assert "error" in response.get_json()

    # Test 'text' not a string
    response = client.post('/strlen', json={"text": 123})
    assert response.status_code == 400
    assert "error" in response.get_json()
