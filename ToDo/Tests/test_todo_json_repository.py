from unittest import TestCase
from ..Repository.todo_json_repository import TodoJsonRepository

class TestTodoJsonRepository(TestCase):
    def test_save_task(self):
        # arrange
        dict_task = {'description':'tache de test2', 'status':'ToDo'}
        # act
        repo = TodoJsonRepository()
        ret = repo.save_task(dict_task)
        # assert
        self.failUnlessRaises()
        self.assertTrue(ret)