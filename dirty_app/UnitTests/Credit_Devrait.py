import unittest
from dirty_app.DomainService.Credit import Credit

class Credit_Devrait(unittest.TestCase):
    def test_cumuler_1(self):
        credit = Credit("1500")
        result = credit.traite("250")
        self.assertEqual("1750.0", result)

    def test_cumuler_2(self):
        input = "0"
        credit = Credit("0")
        result = credit.traite(input)
        self.assertEqual("0", result)

    def test_cumuler_3(self):
        input = "-10"
        credit = Credit("150")
        result = credit.traite(input)
        self.assertEqual("150", result)

    def test_cumuler_4(self):
        input = "12000"
        credit = Credit("500")
        result = credit.traite(input)
        self.assertEqual("500", result)