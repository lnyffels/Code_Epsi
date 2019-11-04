from ..Repository.todo_repository import ToDoRepository
from .todo_save_response_object import ToDoSaveResponseObject

class ToDoSaveUseCase:

    def __init__(self, todo_repo: ToDoRepository):
        self.repository = todo_repo

    def execute(self, request_object):
        self.repository.save(request_object)
        return ToDoSaveResponseObject(True)