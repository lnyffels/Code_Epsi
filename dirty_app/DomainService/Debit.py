
class Debit(object):
    def __init__(self, montant):
        self.f = open("fraude.txt", 'a')
        self.montant = montant


    def traite(self, valeur):
        if not self.isNotNegative(valeur):
            if float(valeur) < 10000:
                self.montant = str(float(self.montant) - float(valeur))
            else:
                self.f.write("alerte mouvement douteux : {} \n".format(valeur))
                self.f.close()
        else:
            print("valeur passée avec un -")
        return self.montant

    def isNotNegative(self, valeur):
        firstCar = str(valeur)[0]
        return firstCar == '-'
