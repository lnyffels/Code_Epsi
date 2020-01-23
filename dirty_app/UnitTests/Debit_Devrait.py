import unittest
from dirty_app.DomainService.Debit import Debit


class Debit_devrait(unittest.TestCase):
    def test_debiter_1(self):
        valeur = "100"
        debit = Debit("2000")
        result = debit.traite(valeur)
        self.assertEqual("1900.0", result)

    def test_debiter_2(self):
        valeur = "-100"
        debit = Debit("1400")
        result= debit.traite(valeur)
        self.assertEqual("1400", result)

    def test_debiter_3(self):
        valeur = "10001"
        debit = Debit("450.55")
        result = debit.traite(valeur)
        self.assertEqual("450.55", result)

