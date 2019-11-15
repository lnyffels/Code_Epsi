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
    try:
        data_task = request.get_json(force=True)
        task_request = ToDoSaveRequestObject(data_task)
        repo = TodoJsonRepository()
        uc = ToDoSaveUseCase(repo)
        response = uc.execute(task_request.get_todo_task())
        return ("{}".format(int(response.return_value)), {"Content-Type": "application/plaintext"})
    except Exception as exc:
        return (str(exc), 400, {})


if __name__ == '__main__':
    app.run(debug=True)
