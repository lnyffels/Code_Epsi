import sqlite3
from ToDo.Repository.todo_repository import ToDoRepository


class TodoDbRepository(ToDoRepository):
    def __init__(self, connection_string):
        self.__conn = sqlite3.connect(connection_string)
        self.__cursor = self.__conn.cursor()

    @property
    def connection(self):
        return self.__conn

    @property
    def cursor(self):
        return self.__cursor

    def create_table(self, sqlCmd):
        self.__execute_commande(sqlCmd)
        return True

    def __execute_commande(self, sqlCommand):
        self.__cursor.execute(sqlCommand)


    def __commit(self):
        self.__conn.commit()

    def save(self, todo_task):
        insertCmd = f"INSERT INTO TODO(description, status) VALUES('{todo_task.description}', '{todo_task.status}')"
        self.__execute_commande(insertCmd)
        self.__commit()
        return True

    def get_all(self):
        pass