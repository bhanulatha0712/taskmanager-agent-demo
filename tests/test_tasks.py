import os
import tempfile

import pytest


@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    import app.storage as storage

    storage.DB_PATH = db_path
    from app.main import create_app

    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client
    os.close(db_fd)
    os.unlink(db_path)


def test_create_and_get_task(client):
    resp = client.post("/tasks", json={"title": "Buy milk"})
    assert resp.status_code == 201
    task = resp.get_json()
    assert task["title"] == "Buy milk"

    resp = client.get(f"/tasks/{task['id']}")
    assert resp.status_code == 200
    assert resp.get_json()["title"] == "Buy milk"


def test_list_tasks(client):
    client.post("/tasks", json={"title": "Task A"})
    client.post("/tasks", json={"title": "Task B"})
    resp = client.get("/tasks")
    assert resp.status_code == 200
    assert len(resp.get_json()) == 2


def test_get_missing_task(client):
    resp = client.get("/tasks/999")
    assert resp.status_code == 404


def test_delete_task(client):
    resp = client.post("/tasks", json={"title": "Temp"})
    task_id = resp.get_json()["id"]
    resp = client.delete(f"/tasks/{task_id}")
    assert resp.status_code == 204
    resp = client.get(f"/tasks/{task_id}")
    assert resp.status_code == 404
