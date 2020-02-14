import datetime
from Exemples.BDD.type_operation import TypeOperation

class Compte:

    def __init__(self, num_compte, nom_compte, type_compte="courant", interets=0.0):
        self.num_compte = num_compte
        self.nom_compte = nom_compte
        self.type_compte = type_compte
        self.interets = interets
        self.liste_operation = []


    def ajouter_operation(self, operation):
        self.liste_operation.append(operation)


    def donner_solde(self):
        solde = 0
        for ope in self.liste_operation:
            if ope.type_operation == str(TypeOperation.CREDIT):
                solde += ope.montant
            else:
                solde -= ope.montant
        return solde

    def __eq__(self, other):
        return ((self.num_compte, self.nom_compte, self.type_compte, self.interets) ==
                (other.num_compte, other.nom_compte, other.type_compte, other.interets))


