import unittest
from ToDo.Repository.todo_db_repository import TodoDbRepository
from ToDo.Domain.todo_task import ToDoTask


class TestTodoDbRepository(unittest.TestCase):

    def setUp(self) -> None:
        self.repo = TodoDbRepository("todo.db")

    def test_init_connection_db(self):
        self.assertIsNotNone(self.repo.connection)

    def test_init_cursor(self):
        self.assertIsNotNone(self.repo.cursor)

    def test_create_table_todo(self):
        sqlCmd = f"CREATE TABLE IF NOT EXISTS TODO(" \
                 f" id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE," \
                 f" description TEXT," \
                 f" status INTEGER )"

        bRet = self.repo.create_table(sqlCmd)
        self.assertTrue(bRet)

    def test_save(self):
        task = ToDoTask("cours python")
        bRet = self.repo.save(task)
        self.assertTrue(bRet)