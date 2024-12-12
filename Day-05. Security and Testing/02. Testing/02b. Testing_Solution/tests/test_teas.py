# tests/test_teas.py

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from models.tea import TeaModel
from tests.lib import login
from main import app

def test_get_teas(test_app: TestClient, override_get_db):
    response = test_app.get("/api/teas")
    assert response.status_code == 200
    teas = response.json()
    assert isinstance(teas, list)
    assert len(teas) is 2
    for tea in teas:
        assert 'id' in tea
        assert 'name' in tea
        assert 'in_stock' in tea
        assert 'rating' in tea
        assert 'user' in tea
        assert 'email' in tea['user']
        assert 'username' in tea['user']
        
def test_get_single_tea(test_app: TestClient, test_db: Session):
    response = test_app.get(f"/api/teas/1")
    assert response.status_code == 200
    tea = response.json()

    assert tea['id'] == 1
    assert tea['name'] == "chai"
    assert tea['in_stock'] == True
    assert tea['rating'] == 4

def test_get_single_tea_not_found(test_app: TestClient):
    response = test_app.get("/api/teas/9999")  # Assuming there's no tea with id 9999
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}        

def test_create_tea(test_app: TestClient, test_db: Session):
    headers = login(test_app, 'ben')

    tea_data = {
        "name": "Test Tea",
        "in_stock": True,
        "rating": 4
    }

    response = test_app.post("/api/teas", headers=headers, json=tea_data)

    # Assert that the tea was created
    assert response.status_code == 200

    # # Assert that the returned data matches the tea_data
    assert response.json()["name"] == tea_data["name"]
    assert response.json()["in_stock"] == tea_data["in_stock"]
    assert response.json()["rating"] == tea_data["rating"]
    assert "id" in response.json()
    assert "user" in response.json()
    assert response.json()['user']["username"] == 'ben'

    # Now, check if the tea was actually created in the database:
    tea_id = response.json()["id"]
    tea = test_db.query(TeaModel).filter(TeaModel.id == tea_id).first()

    # Assert that the tea is not None (meaning it exists in the DB)
    assert tea is not None

    # Assert that the tea in the DB has the same data as what we sent
    assert tea.name == tea_data["name"]
    assert tea.in_stock == tea_data["in_stock"]
    assert tea.rating == tea_data["rating"]
    
def test_get_single_tea(test_app: TestClient, test_db: Session):
    response = test_app.get(f"/api/teas/1")
    assert response.status_code == 200
    tea = response.json()

    assert tea['id'] == 1
    assert tea['name'] == "chai"
    assert tea['in_stock'] == True
    assert tea['rating'] == 4.3
    
def test_create_tea_not_logged_in(test_app: TestClient, test_db: Session):

    tea_data = {
        "name": "Test Tea",
        "in_stock": True,
        "rating": 4
    }

    response = test_app.post("/api/teas", json=tea_data)

    # Assert that this operation was restricted
    assert response.status_code == 403

    assert response.json() == {'detail': 'Not authenticated'}

def test_update_tea(test_app: TestClient, test_db: Session):
    headers = login(test_app, 'ben')

    tea_data = {
        "name": "Test with name change!",
        "in_stock": True,
        "rating": 4
    }

    response = test_app.put("/api/teas/3", headers=headers, json=tea_data)

    # Assert that the tea was updated
    assert response.status_code == 200

    # # Assert that the returned data matches the tea_data
    assert response.json()["name"] == tea_data["name"]
    assert response.json()["in_stock"] == tea_data["in_stock"]
    assert response.json()["rating"] == tea_data["rating"]
    assert "id" in response.json()
    assert "user" in response.json()
    assert response.json()['user']["username"] == 'ben'

    # Now, check if the tea was actually updated in the database:
    tea_id = response.json()["id"]
    tea = test_db.query(TeaModel).filter(TeaModel.id == tea_id).first()

    # Assert that the tea is not None (meaning it exists in the DB)
    assert tea is not None

    # Assert that the tea in the DB has the same data as what we sent
    assert tea.name == tea_data["name"]
    assert tea.in_stock == tea_data["in_stock"]
    assert tea.rating == tea_data["rating"]

def test_update_restricted(test_app: TestClient, test_db: Session):
    headers = login(test_app, 'ben')

    tea_data = {
        "name": "Test with name change!",
        "in_stock": True,
        "rating": 4
    }

    response = test_app.put("/api/teas/2", headers=headers, json=tea_data)

    # Assert that this operation was restricted
    assert response.status_code == 403
    
    assert response.json() == {'detail': 'Operation forbidden'}

def test_update_not_found(test_app: TestClient, test_db: Session):
    headers = login(test_app, 'ben')

    tea_data = {
        "name": "Test with name change!",
        "in_stock": True,
        "rating": 4
    }

    response = test_app.put("/api/teas/999999", headers=headers, json=tea_data)

    # Assert that record was not found
    assert response.status_code == 404
    
    assert response.json() == {'detail': 'Item not found'}
  
def test_delete_tea(test_app: TestClient, test_db: Session):
    headers = login(test_app, 'ben')

    response = test_app.delete("/api/teas/3", headers=headers)

    # Assert that the tea was deleted
    assert response.status_code == 200
    assert response.json() == {'message': 'Tea 3 deleted successfully'}

    # Now, check if the tea is in the database:
    tea = test_db.query(TeaModel).filter(TeaModel.id == 3).first()

    # Assert that the tea is None (meaning it was deleted from DB)
    assert tea is None

def test_delete_tea_not_found(test_app: TestClient, test_db: Session):
    headers = login(test_app, 'ben')

    response = test_app.delete("/api/teas/999999", headers=headers)

    # Assert that the tea is not found
    assert response.status_code == 404
    assert response.json() == {'detail': 'Item not found'}

def test_delete_tea_restricted(test_app: TestClient, test_db: Session):
    headers = login(test_app, 'ben')

    response = test_app.delete("/api/teas/2", headers=headers)

    # Assert that operation was forbidden
    assert response.status_code == 403
    assert response.json() == {'detail': 'Operation forbidden'}