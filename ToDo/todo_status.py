from enum import Enum

class ToDoStatus(Enum):
    TODO = 0
    IN_PROGRESS = 1
    DONE = 2

    def __str__(self):
        if self == ToDoStatus.TODO:
            return "ToDo"
        elif self == ToDoStatus.IN_PROGRESS:
            return "In Progress"
        elif self == ToDoStatus.DONE:
            return "Done"
        else:
            raise Exception("Valeur en dehors de l'enumération")
