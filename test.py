import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'
tasks = []


def test_create_task():
    task_data_json = {
        "title" : "teste",
        "description" : "descrição do teste"
    }
    response = requests.post(f"{BASE_URL}/tasks", json= task_data_json)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json["id"])


def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json


def test_get_task():
    if tasks:
        task_id = tasks[0]
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200
    response_json = response.json()
    assert task_id == response_json["id"]


def test_update_task():
    update_task_data = {
        "title" : "Atualizando a tarefa",
        "description" : "descrição",
        "completed" : True
    }
    if tasks:
        task_id = tasks[0]
    response = requests.put(f"{BASE_URL}/tasks/{task_id}", json = update_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in  response_json

    get_response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    get_response_json = get_response.json()
    assert update_task_data["title"] == get_response_json["title"]
    assert update_task_data["description"] == get_response_json["description"]
    assert update_task_data["completed"] == get_response_json["completed"]


def test_delete_task():
    data = {
        "title" : "titulo",
        "description" : "descrição"
    }

    reponse_create =  requests.post(f"{BASE_URL}/tasks", json= data)
    assert reponse_create.status_code == 200

    if tasks:
        task_id = tasks[0]
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json

    if not tasks:
        response = requests.get(f"{BASE_URL}/tasks")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["total_tasks"] == 0