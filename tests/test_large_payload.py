import pytest
from flask_echo_server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_string_length_large_payload(client):
    """Tests the string_length endpoint with a 1GB payload."""

    one_kb = 1024
    one_mb = one_kb * one_kb
    one_gb = one_mb * one_kb

    class LargePayload:
        def __init__(self, size, chunk_size=one_mb):
            self.size = size
            self.chunk_size = chunk_size
            self.read_so_far = 0

        def read(self, size):
            if self.read_so_far >= self.size:
                return b''

            remaining = self.size - self.read_so_far
            size_to_read = min(size, remaining, self.chunk_size)

            self.read_so_far += size_to_read
            return b'a' * size_to_read

        def __len__(self):
            return self.size

        def tell(self):
            return self.read_so_far

        def seek(self, offset, whence=0):
            if whence == 0:
                self.read_so_far = offset
            elif whence == 1:
                self.read_so_far += offset
            elif whence == 2:
                self.read_so_far = self.size + offset
            return self.read_so_far


    payload = LargePayload(one_gb)
    response = client.post(
        '/string_length',
        input_stream=payload,
        content_length=len(payload),
    )
    assert response.status_code == 200
    assert response.get_json() == {"length": one_gb}
