from fastapi.testclient import TestClient
from models.todo import Todo
from app.app import app


client = TestClient(app)


# we can use baseclass entity to fix this problem ...

def test_get_todos():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == []


def test_create_todo():
    response = client.post("/", json={"name": "foobar", "description": "Foo Bar", "complete": False})
    assert response.status_code == 200
    assert response.json() == {
        "data": {"name": "foobar", "description": "Foo Bar", "complete": False}
    }


def test_update_todo(user_id):
    user_id = '65903f6542d0354997a7caf9'
    sample_payload = {"name": "foobar", "description": "Foo Barrr", "complete": False}
    response = client.put(f"/{user_id}", json=sample_payload)
    assert response.status_code == 200
    assert response.json() == {
        "data": {"name": "foobar", "description": "Foo Barrr", "complete": False}
    }


def test_delete_todo(user_id):
    user_id = '65903f6542d0354997a7caf9'
    response = client.delete(f"/{user_id}")
    assert response.status_code == 200
    assert response.json() == {
        "data": user_id
    }

