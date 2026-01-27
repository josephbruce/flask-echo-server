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
    response = client.get('/strlen?text=hello')
    assert response.status_code == 200
    assert response.get_json() == {"len": 5}

def test_strlen_empty(client):
    response = client.get('/strlen?text=')
    assert response.status_code == 200
    assert response.get_json() == {"len": 0}

def test_strlen_missing_param(client):
    # Depending on implementation, this might be 400 or just return None/0 or error
    # Let's assume we want it to handle it gracefully or error.
    # For now, I'll expect a 200 and maybe len 0 or None if I use request.args.get('text', '')
    response = client.get('/strlen')
    # If we default to empty string
    assert response.status_code == 200
    assert response.get_json() == {"len": 0}
