from unittest import TestCase
from ..todo_status import ToDoStatus

class TestToDoStatus(TestCase):
    def test_all_status(self):
        self.assertEqual("Done", str(ToDoStatus.DONE))
        self.assertEqual("In Progress", str(ToDoStatus.IN_PROGRESS))
        self.assertEqual("ToDo", str(ToDoStatus.TODO))


