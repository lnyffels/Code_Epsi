import datetime

class Compte:

    def __init__(self, num_compte, nom_compte, date_solde=datetime.datetime.now(), type_compte="courant", interets=0.0):
        self.num_compte = num_compte
        self.nom_compte = nom_compte
        self.date_solde = datetime.datetime.now()
        self.type_compte = type_compte
        self.interets = interets
        self.liste_operation = []


    def ajouter_operation(self, operation):
        self.liste_operation.append(operation)


    def donner_solde(self):
        solde = 0
        for ope in self.liste_operation:
            if ope.type_operation == "C":
                solde += ope.montant
            else:
                solde -= ope.montant
        return solde



