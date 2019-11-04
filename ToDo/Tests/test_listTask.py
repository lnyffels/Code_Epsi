from unittest import TestCase
from ToDo.Domain.list_task import ListTask

class TestListTask(TestCase):

    def setUp(self):
        self.lst = ListTask()

    def test_add_item(self):
        nb_elem_initial = self.lst.count_all_items()
        self.lst.add_item("tache1")
        self.assertEqual(self.lst.count_all_items(), nb_elem_initial+1)


    def test_get_all_item(self):
        liste_vide = ListTask()
        self.lst.add_item("T1")
        self.lst.add_item("T2")
        dico_tache = self.lst.get_all_item()
        self.assertEqual(len(dico_tache), 2)
