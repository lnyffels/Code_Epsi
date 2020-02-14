import unittest
from unittest import mock
from Exemples.BDD import (client as clt, api_banque as b)
from Exemples.BDD.api_banque import APIBanque


class TestCompte(unittest.TestCase):
    def test_liste_comptes_client(self):
        # arrange
        client = clt.Client("lnf", "azerty", "158568")
        # Simulation appel API Banque
        api_response = {
            "num_client": "158568",
            "count": 3,
            "comptes": [
                {
                    "num_compte": "123",
                    "nom_compte": "compte courant",
                    "type_compte": "courant",
                    "interets" :"0"
                },
                {
                    "num_compte": "456",
                    "nom_compte": "CEL",
                    "type_compte": "epargne",
                    "interets": "0.5"
                },
                {
                    "num_compte": "789",
                    "nom_compte": "PEL",
                    "type_compte": "epargne",
                    "interets": "1.25"
                }
            ]
        }

        # act
        api = b.APIBanque()
        api.get_liste_comptes = mock.Mock()
        api.get_liste_comptes.return_value = api_response

        # assert
        self.assertEqual(api.get_nb_compte(158568), 3)


if __name__ == '__main__':
    unittest.main()
