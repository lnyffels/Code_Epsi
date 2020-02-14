from Exemples.BDD import (operation as o, compte as c, type_operation)

class CompteVirerUsecase(object):

    def transfer(self, montant: float, compte_courant : c.Compte, compte_epargne: c.Compte):
        compte_courant.ajouter_operation(o.Operation(montant,"virement débit", "D"))
        compte_epargne.ajouter_operation(o.Operation(montant,"virement crédit", "C"))
