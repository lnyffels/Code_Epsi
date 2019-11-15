from ..Tools.TodoJsonEncoder import TodoJsonEncoder
from ToDo.Repository.todo_repository import ToDoRepository
import json

class TodoJsonRepository(ToDoRepository):

    def save(self, todo_task):
        try:
            with open('todo_data.json', 'a') as f:  # externaliser
                str_task = json.dumps(todo_task, cls=TodoJsonEncoder)
                f.write(str_task)
            return True
        except Exception as exc:
            print(exc)
            raise exc

    def get_all(self):
        pass