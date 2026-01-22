import pytest
from flask_echo_server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_strlen_basic(client):
    response = client.post('/strlen', json={"text": "hello"})
    assert response.status_code == 200
    assert response.get_json() == {"len": 5}

def test_strlen_empty(client):
    response = client.post('/strlen', json={"text": ""})
    assert response.status_code == 200
    assert response.get_json() == {"len": 0}
