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

def test_madlibs_success(client):
    response = client.get('/madlibs?place=store&verb=shop')
    assert response.status_code == 200
    assert response.get_json() == {"sentence": "I went to the store so I could shop"}

def test_madlibs_missing_params(client):
    response = client.get('/madlibs?place=store')
    assert response.status_code == 400
    assert response.get_json() == {"error": "Both 'place' and 'verb' query parameters are required."}

    response = client.get('/madlibs?verb=shop')
    assert response.status_code == 400
    assert response.get_json() == {"error": "Both 'place' and 'verb' query parameters are required."}

    response = client.get('/madlibs')
    assert response.status_code == 400
    assert response.get_json() == {"error": "Both 'place' and 'verb' query parameters are required."}
