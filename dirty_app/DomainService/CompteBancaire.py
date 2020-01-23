class CompteBancaire(object):
    def __init__(self, listeOperations):
        self.operations = listeOperations

    def getOperations(self, dateDebut, datefin):
        liste = []
        for operation in self.operations:
            trouve = False
            if operation.dateValeur > dateDebut:
                if operation.dateValeur < datefin:
                    trouve = True
            if trouve:
                liste.append(operation)
        return liste
