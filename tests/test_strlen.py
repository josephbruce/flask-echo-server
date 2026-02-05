import pytest
from flask_echo_server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_strlen_success(client):
    response = client.post('/strlen', json={"message": "hello"})
    assert response.status_code == 200
    assert response.get_json() == {"strlen": 5}

def test_strlen_empty_string(client):
    response = client.post('/strlen', json={"message": ""})
    assert response.status_code == 200
    assert response.get_json() == {"strlen": 0}

def test_strlen_missing_key(client):
    response = client.post('/strlen', json={})
    assert response.status_code == 200
    assert response.get_json() == {"strlen": 0}

def test_strlen_non_string_value(client):
    response = client.post('/strlen', json={"message": 123})
    assert response.status_code == 200
    # Implementation casts to string, so "123" length is 3
    assert response.get_json() == {"strlen": 3}

def test_strlen_non_json_payload(client):
    response = client.post('/strlen', data="not json", content_type='text/plain')
    assert response.status_code == 200
    assert response.get_json() == {"strlen": 0}
