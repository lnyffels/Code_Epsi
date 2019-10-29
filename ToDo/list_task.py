from ToDo.todo_task import ToDoTask
from ToDo.todo_status import ToDoStatus

class ListTask:
    def __init__(self):
        self.__dico = {}
        self.__idx = 0

    def count_all_items(self):
        return len(self.__dico)

    def add_item(self, description):
        idx = self.__idx
        self.__dico[idx] = ToDoTask(description)
        self.__idx += 1

    def get_all_item(self):
        return self.__dico.values()