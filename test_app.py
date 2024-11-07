import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test if the home page loads correctly"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"This is the home page." in response.data

def test_about_page(client):
    """Test if the about page loads correctly"""
    response = client.get('/about')
    assert response.status_code == 200
    assert b"About Me" in response.data  
    assert b"I'm Hamza Adam Aliyu" in response.data
  

def test_contact_page(client):
    """Test if the contact page loads correctly"""
    response = client.get('/contact')
    assert response.status_code == 200
    assert b"This is my contact page" in response.data  
