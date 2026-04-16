import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'

# Testando o endpoint CREATE TASK
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

# Testando o endpoint GET TASKS
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

# Testando o endpoint GET TASK
def test_get_task():
    new_task_data = {
        "title" : "Teste",
        "description" : "Descrição"
    }
    response_create = requests.post(f"{BASE_URL}/tasks", json= new_task_data)
    assert response_create.status_code == 200
    response_create_json = response_create.json()
    assert "message" in response_create_json
    assert "id" in response_create_json

    response_get = requests.get(f"{BASE_URL}/tasks/{response_create_json["id"]}")
    assert response_get.status_code == 200
    response_get_json = response_get.json()

#Testando o endpoint UPDATE TASK
def test_update_task():
    new_task_data = {
        "title" : "Teste",
        "description" : "Descrição"
    }
    response_create = requests.post(f"{BASE_URL}/tasks", json= new_task_data)
    assert response_create.status_code == 200
    response_create_json = response_create.json()
    assert "message" in response_create_json
    assert "id" in response_create_json

    update_task_data = {
        "title" : "Atualizando a tarefa",
        "description" : "descrição",
        "completed" : True
    }
    
    response_update = requests.put(f"{BASE_URL}/tasks/{response_create_json["id"]}", json = update_task_data)
    assert response_update.status_code == 200
    response_update_json = response_update.json()
    assert "message" in  response_update_json

    response_get = requests.get(f"{BASE_URL}/tasks/{response_create_json["id"]}")
    response_get_json = response_get.json()
    assert update_task_data["title"] == response_get_json["title"]
    assert update_task_data["description"] == response_get_json["description"]
    assert update_task_data["completed"] == response_get_json["completed"]

# Testando o endpoint DELETE TASK
def test_delete_task():
    new_task_data = {
        "title" : "titulo",
        "description" : "descrição"
    }
    response_create = requests.post(f"{BASE_URL}/tasks", json= new_task_data)
    assert response_create.status_code == 200
    response_create_json = response_create.json()
    assert "message" in response_create_json
    assert "id" in response_create_json

    
    response_delete = requests.delete(f"{BASE_URL}/tasks/{response_create_json["id"]}")
    assert response_delete.status_code == 200
    response_delete_json = response_delete.json()
    assert "message" in response_delete_json
    
    response_get_task = requests.get(f"{BASE_URL}/tasks/{response_create_json["id"]}")
    assert response_get_task.status_code == 404