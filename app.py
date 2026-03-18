from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id= task_id_control, title= data["title"], description= data.get("description", ""))
    tasks.append(new_task)
    task_id_control += 1
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso"})


@app.route("/tasks", methods= ["GET"])
def get_tasks():
    tasks_list = [task.to_dict() for task in tasks]
    output = {
        "tasks": tasks_list,
        "total_tasks": len(tasks_list)
    }
    return jsonify(output)


@app.route("/tasks/<int:id>", methods= ["GET"])
def get_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({"message": "Não foi possivel encontrar a tarefa"}), 404


@app.route("/tasks/<int:id>", methods= ["PUT"])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    print(task)

    if task == None:
        return jsonify({"message": "Não foi possivel encontrar a tarefa"}), 404
    
    data = request.get_json()
    task.title = data["title"]
    task.description = data["description"]
    task.completed = data["completed"]
    print(task)
    return jsonify({"message": "Tarefa atualizada com sucesso!"})




if __name__ == "__main__":
    app.run(debug=True)