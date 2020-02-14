from Exemples.BDD.compte import Compte

class APIBanque:
    def __init__(self):
        pass

    def get_liste_comptes(self, num_client):
        #pass
        return [Compte("123", "compte courant", "courant", 0.00), Compte("456", "CEL", "epargne", 0.50)]

    def get_nb_compte(self, num_client):
        data = self.get_liste_comptes(num_client)
        return int(data["count"])

