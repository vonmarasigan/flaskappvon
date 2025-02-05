from urllib import response
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_greetme(client):
    response = client('/')
    assert response.data==b'Hello Deveops'
    assert response.status==200


def test_page1(client):
    response = client('/page1')
    assert response.data==b'welcome to page1'
    assert response.status==200
