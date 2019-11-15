import abc

class ToDoRepository(abc.ABC):

    # @abc.abstractmethod
    # def get(self, id_todo):
    #     pass

    @abc.abstractmethod
    def save(self, todo_task):
        pass

    @abc.abstractmethod
    def get_all(self):
        pass
