from flask import Flask, request
from ToDo.UseCase.todo_save_usecase import ToDoSaveUseCase
from ToDo.UseCase.todo_save_request_object import ToDoSaveRequestObject
from ToDo.Repository.todo_json_repository import TodoJsonRepository

app = Flask(__name__)


@app.route('/')
def home():
    return "Home page"

@app.route("/add", methods=['POST'])
def add():
    data_task = request.get_json(force=True)
    if "description" not in data_task:
        return ("description manquante", 400, {})

    task = ToDoSaveRequestObject(data_task["description"])
    repo = TodoJsonRepository()
    uc = ToDoSaveUseCase(repo)
    response = uc.execute(task)
    return ("{}".format(int(response.return_value)), {"Content-Type": "application/plaintext"})

if __name__ == '__main__':
    app.run(debug=True)
