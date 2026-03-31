import pytest
from app import app, add, divide

def test_add():
    assert add(10, 5) == 15
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(10, 0) is None

def test_calculate_route():
    client = app.test_client()
    response = client.get('/calculate')
    assert response.status_code == 200
    assert response.json['result'] == 15
