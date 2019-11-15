from ToDo.Domain.todo_status import ToDoStatus

class ToDoTask:
    def __init__(self, description):
        self.__description = description
        self.__status = ToDoStatus.TODO

    @property
    def description(self):
        return  self.__description

    @property
    def status(self):
        return self.__status

    def to_dict(self):
        return {
            'description': self.__description,
            'status': str(self.__status)
        }