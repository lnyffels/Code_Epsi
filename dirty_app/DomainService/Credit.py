import datetime

class Credit:
    def __init__(self, valeur):
        print("valeur de ".format(valeur))
        self.valeur = valeur

    def traite(self, entrée):
        if float(entrée) > 0 and float(entrée) < 10000 and datetime.datetime.today().weekday() != 6:
            print("valeur de ".format(entrée))
            self.valeur = str(float(self.valeur) + float(entrée))
        if entrée == "0":
            return "0"
        return self.valeur