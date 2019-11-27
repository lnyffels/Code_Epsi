import unittest
import datetime
from Exemples.BDD.compte import Compte
from Exemples.BDD.operation import Operation


class TestCompte(unittest.TestCase):

    def test_ajouter_operation(self):
        compte_courant = Compte(1234, "CPT_COURANT", datetime.datetime.now(), "C", 0)
        operation_credit = Operation(100, "depot cheque", "C")
        compte_courant.ajouter_operation(operation_credit)
        operation_debit = Operation(15, "achat fleur", "D")
        compte_courant.ajouter_operation(operation_debit)
        self.assertEqual(len(compte_courant.liste_operation), 2)

    def test_donner_solde(self):
        compte_courant = Compte(1234, "CPT_COURANT", datetime.datetime.now(), "C", 0)
        operation1 = Operation(100, "depot cheque", "C")
        compte_courant.ajouter_operation(operation1)
        operation2 = Operation(50, "achat fleur", "D")
        compte_courant.ajouter_operation(operation2)
        operation3 = Operation(60, "depot", "C")
        compte_courant.ajouter_operation(operation3)
        nouveau_solde = compte_courant.donner_solde()
        self.assertEqual(nouveau_solde, 110)

if __name__ == '__main__':
    unittest.main()
