from ..Domain.todo_task import ToDoTask
from ..Domain.list_task import ListTask
from ..Domain.todo_status import ToDoStatus
from ToDo.Repository.todo_repository import ToDoRepository
import json

class TodoJsonRepository(ToDoRepository):
    def save(self, todo_task):
        try:
            with open('c:\\todo_data.json', 'a') as f:  # externaliser
                json.dump(todo_task, f)
            return True
        except:
            raise Exception("erreur enregistrement fichier json")

    def get_all(self):
        pass