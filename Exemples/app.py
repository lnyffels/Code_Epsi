class OpenFoodFactsAPI:
    """
    Cette classe a pour objectif de récupérer les produits associée à une marque
    via l'API d'OpenFoodFacts et de compter le nombre de produits ayant une bonne
    note alimentaire.
    """
    def __init__(self):
        pass

    def _get_product_from_api(self, brand):
        pass

    def count_product_numb(self, brand):
        """
                Cette méthode a pour objectif de dénombrer le nombre de produits ayant
                une bonne note alimentaire
                Il s'agit de la méthode à tester pour cette exercice
                """

        data = self._get_product_from_api(brand)
        healthy_product = 0
        for product in data["products"]:
            try:
                if product["nutrition_grade_fr"] == "a":
                    healthy_product += 1
            except:
                pass

        return healthy_product