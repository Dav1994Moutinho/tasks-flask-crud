import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'


def test_create_task():
    new_task_data = {
        "title" : "teste",
        "description" : "descrição do teste"
    }
    response = requests.post(f"{BASE_URL}/tasks", json= new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json


def test_get_tasks():
    new_task_data = {
        "title" : "teste",
        "description" : "Descrição"
    }
    response_create = requests.post(f"{BASE_URL}/tasks", json= new_task_data)
    assert response_create.status_code == 200
    response_create_json = response_create.json()
    assert "message" in response_create_json
    assert "id" in response_create_json

    response_get = requests.get(f"{BASE_URL}/tasks")
    assert response_get.status_code == 200
    response_get_json = response_get.json()
    assert "tasks" in response_get_json
    assert "total_tasks" in response_get_json


def test_get_task():
    tasks_test = []
    new_task_data = {
        "title" : "Teste",
        "description" : "Descrição"
    }
    response_create = requests.post(f"{BASE_URL}/tasks", json= new_task_data)
    assert response_create.status_code == 200
    response_create_json = response_create.json()
    assert "message" in response_create_json
    assert "id" in response_create_json
    tasks_test.append(response_create_json["id"])

    if tasks_test:
        task_id = tasks_test[0]
    response_get = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response_get.status_code == 200
    response_get_json = response_get.json()
    assert task_id == response_get_json["id"]


def test_update_task():
    tasks_test = []
    new_task_data = {
        "title" : "Teste",
        "description" : "Descrição"
    }
    response_create = requests.post(f"{BASE_URL}/tasks", json= new_task_data)
    assert response_create.status_code == 200
    response_create_json = response_create.json()
    assert "message" in response_create_json
    assert "id" in response_create_json
    tasks_test.append(response_create_json["id"])

    update_task_data = {
        "title" : "Atualizando a tarefa",
        "description" : "descrição",
        "completed" : True
    }
    if tasks_test:
        task_id = tasks_test[0]
    response_update = requests.put(f"{BASE_URL}/tasks/{task_id}", json = update_task_data)
    assert response_update.status_code == 200
    response_update_json = response_update.json()
    assert "message" in  response_update_json

    response_get = requests.get(f"{BASE_URL}/tasks/{task_id}")
    response_get_json = response_get.json()
    assert update_task_data["title"] == response_get_json["title"]
    assert update_task_data["description"] == response_get_json["description"]
    assert update_task_data["completed"] == response_get_json["completed"]


def test_delete_task():
    tasks_test = []
    new_task_data = {
        "title" : "titulo",
        "description" : "descrição"
    }
    response_create = requests.post(f"{BASE_URL}/tasks", json= new_task_data)
    assert response_create.status_code == 200
    response_create_json = response_create.json()
    assert "message" in response_create_json
    assert "id" in response_create_json
    tasks_test.append(response_create_json["id"])

    if tasks_test:
        task_id = tasks_test[0]
    response_delete = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    assert response_delete.status_code == 200
    response_delete_json = response_delete.json()
    assert "message" in response_delete_json

    if not tasks_test:
        response_get = requests.get(f"{BASE_URL}/tasks")
        assert response_get.status_code == 200
        response_get_json = response_get.json()
        assert response_get_json["total_tasks"] == 0