from unittest import TestCase
from ..todo_task import ToDoTask


class TestToDoTask(TestCase):
    def test_to_dict(self):
        task = ToDoTask("tache 1")
        dict_task = {"description": "tache 1", "status": "ToDo"}
        dic = task.to_dict()
        self.assertEqual(dict_task["description"], dic["description"])
        self.assertEqual(dict_task["status"], dic["status"])

    def test_description(self):
        task= ToDoTask("tache de test")
        self.assertEqual(task.description, "tache de test")

    def test_status(self):
        task= ToDoTask("tache de test")
        self.assertEqual(str(task.status), "ToDo")
