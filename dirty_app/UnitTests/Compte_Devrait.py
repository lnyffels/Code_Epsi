import unittest
import datetime
from dirty_app.DomainService.OperationBancaire import *
from dirty_app.DomainService.CompteBancaire import *


class Compte_Devrait(unittest.TestCase):

    def setUp(self):
        operationEnMars = OperationBancaire(datetime.datetime(2019, 3, 10))
        operationEnAvril = OperationBancaire(datetime.datetime(2019, 4, 20))
        operationEnMai = OperationBancaire(datetime.datetime(2019, 5, 8))
        operationEnJuin = OperationBancaire(datetime.datetime(2019, 5, 29))
        lst = [operationEnMars, operationEnAvril, operationEnMai, operationEnJuin]
        self.cpt = CompteBancaire(lst)

    def test_return_operations_beetween_date(self):
        dtDebut = datetime.datetime(2019, 3, 20)
        dtFin = datetime.datetime(2019, 5, 17)
        lstOp = self.cpt.getOperations(dtDebut, dtFin)
        self.assertEqual(2, len(lstOp))
