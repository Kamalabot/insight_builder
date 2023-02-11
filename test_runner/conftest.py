"""Creates the test fixture necessary for API testing"""
from fastapi.testclient import TestClient
import pytest
from server.server import app

@pytest.fixture()
def vanilla_session():
    """Tests the base route of the server"""
    print('Raw session started')
    yield TestClient(app)
