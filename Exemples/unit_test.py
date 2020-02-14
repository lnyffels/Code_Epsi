import unittest
from unittest import mock
from Exemples.app import OpenFoodFactsAPI


class Personne:
    def __init__(self):
        pass

    def donner_nom_personne(self, matricule):
        pass
        # return f'Toto, matricule {matricule}'


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setup")

    def test_magicMock_returvalue(self):
        lnf = Personne()
        mock_2 = mock.MagicMock(return_value="moooook")
        lnf.donner_nom_personne = mock_2()  # Création d'un mock sur la méthode "donner_nom_personne"
        val_ret = lnf.donner_nom_personne  # retourne "moooook"
        self.assertEqual(lnf.donner_nom_personne, "moooook")  # S'assurer que la méthode retourne bien "moooook"

    def test_count_product_numb(self):

        api_response = {
            "count": 6,
            "skip": 0,
            "page_size": "150",
            "page": 1,
            "products": [
                {
                    "product_name_fr": "Ferrero boite de 30",
                    "nutrition_grade_fr": "a",
                },
                {
                    "product_name_fr": "Ferrero Light sans sucre et sans goût",
                    "nutrition_grade_fr": "b",
                },
                {
                    "product_name_fr": "Ferrero Rocher",
                    "nutrition_grade_fr": "e",
                },
                {
                    "product_name_fr": "Ferrero couscous",
                    "nutrition_grade_fr": "a",
                },
                {
                    "product_name_fr": "Ferrero chocolat praliné",
                    "nutrition_grade_fr": "d",
                },
                {
                    "product_name_fr": "Ferrero à la fraise",
                    "nutrition_grade_fr": "c",
                },
            ]
        }

        healthy_product = OpenFoodFactsAPI()
        healthy_product._get_product_from_api = mock.Mock()
        healthy_product._get_product_from_api.return_value = api_response

        self.assertEqual(healthy_product.count_product_numb("ferrero"), 2)

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown")

if __name__ == '__main__':
    unittest.main()
