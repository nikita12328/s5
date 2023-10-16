from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Подготовка данных для тестирования
sample_task = {
    "title": "Test Task",
    "description": "Test Description",
    "status": False
}


def test_create_task():
    response = client.post("/tasks/", json=sample_task)
    assert response.status_code == 200
    task = response.json()
    assert task["title"] == sample_task["title"]


def test_read_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    tasks = response.json()
    assert isinstance(tasks, list)
    assert len(tasks) > 0


def test_read_task():
    response = client.get("/tasks/0")
    assert response.status_code == 200
    task = response.json()
    assert task["title"] == sample_task["title"]


def test_update_task():
    updated_task = {"title": "Updated Task", "description": "Updated Description", "status": True}
    response = client.put("/tasks/0", json=updated_task)
    assert response.status_code == 200
    task = response.json()
    assert task["title"] == updated_task["title"]


def test_delete_task():
    response = client.delete("/tasks/0")
    assert response.status_code == 200
    deleted_task = response.json()
    assert deleted_task["title"] == "Updated Task"
