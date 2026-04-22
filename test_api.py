import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"etat": "bon"}

def test_get_alltasks(client):
    res = client.get("/api/v1/tasks")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_create_task(client):
    payload = {
        "title": "test",
        "description": "test",
        "priority": 0,
        "due_date": "2029-01-01T00:00:00",
        "status": True
    }

    response = client.post("/api/v1/tasks", json=payload)

    assert response.status_code == 200
    assert response.json()["title"] == "test"
    assert response.json()["description"] == "test"
    assert response.json()["priority"] == 0
    assert response.json()["status"] == True

def test_get_task_by_id(client):
    payload = {
        "title": "test task",
        "description": "test description",
        "priority": 1,
        "due_date": "2029-06-15T00:00:00",
        "status": True
    }
    
    create_response = client.post("/api/v1/tasks", json=payload)
    task_id = create_response.json()["_id"]
    
    get_response = client.get(f"/api/v1/task/{task_id}")
    assert get_response.status_code == 200
    assert get_response.json()["_id"] == task_id
    assert get_response.json()["title"] == "test task"

def test_update_task(client):
    payload = {
        "title": "original task",
        "description": "original description",
        "priority": 0,
        "due_date": "2029-01-01T00:00:00",
        "status": True
    }
    
    create_response = client.post("/api/v1/tasks", json=payload)
    task_id = create_response.json()["_id"]
    
    update_payload = {
        "title": "updated task",
        "description": "updated description",
        "priority": 2,
        "due_date": "2029-12-31T00:00:00",
        "status": False
    }
    
    update_response = client.put(f"/api/v1/task/{task_id}", json=update_payload)
    assert update_response.status_code == 200
    assert update_response.json()["title"] == "updated task"
    assert update_response.json()["priority"] == 2
    assert update_response.json()["status"] == False

def test_delete_task(client):
    payload = {
        "title": "task to delete",
        "description": "this will be deleted",
        "priority": 1,
        "due_date": "2029-01-01T00:00:00",
        "status": True
    }
    
    create_response = client.post("/api/v1/tasks", json=payload)
    task_id = create_response.json()["_id"]
    
    delete_response = client.delete(f"/api/v1/task/{task_id}")
    assert delete_response.status_code == 200
    
    get_response = client.get(f"/api/v1/task/{task_id}")
    assert get_response.status_code == 404
