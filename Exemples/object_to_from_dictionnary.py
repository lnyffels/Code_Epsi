class Adresse:
    def __init__(self, rue, ville, cp):
        self.rue = rue
        self.ville = ville
        self.cp = cp

    def to_dict(self):
        return {
            "rue": self.rue,
            "ville": self.ville,
            "cp": self.cp
        }

    @classmethod
    def from_dict(cls, dico):
        return cls(
            rue=dico["rue"],
            ville=dico["ville"],
            cp=dico["cp"]
        )


class Compte:
    def __init__(self, typeCompte, solde):
        self.typeCompte = typeCompte
        self.solde = solde

    def to_dict(self):
        return {
            "TypeCompte": self.typeCompte,
            "Solde": self.solde
        }

    @classmethod
    def from_dict(cls, dico):
        return cls(
            typeCompte=dico["TypeCompte"],
            solde=dico["Solde"]
        )


class Personne:
    def __init__(self, nom, adresse, liste_compte=[]):
        self.nom = nom
        self.adresse = adresse
        self.liste_compte = liste_compte

    def ajouter_compte(self, compte):
        self.liste_compte.append(compte)

    def to_dict(self):
        return {
            "nom": self.nom,
            "adresse": self.adresse.to_dict(),
            "liste_compte": [c.to_dict() for c in self.liste_compte]
        }

    @classmethod
    def _liste_compte(cls, liste_compte_dict):
        lst = []
        for dict_compte in liste_compte_dict:
            compte = Compte.from_dict(dict_compte)
            lst.append(compte)
        return lst

    @classmethod
    def from_dict(cls, dico):
        return cls(
            nom= dico["nom"],
            adresse = Adresse.from_dict(dico["adresse"]),
            liste_compte= cls._liste_compte([dic for dic in dico["liste_compte"]])
        )


dic_init_compte = {'nom': 'nyffels', 'adresse': {'rue': '4 rue de la paie', 'ville': 'Lille', 'cp': 59}, 'liste_compte': [{'TypeCompte': 'courant', 'Solde': 100.0}, {'TypeCompte': 'Epargne', 'Solde': 34.5}]}
pers = Personne.from_dict(dic_init_compte)
print(pers)


address = Adresse("4 rue de la paie", "Lille", 59)
pers = Personne("nyffels", address)
compteCourant = Compte("courant", 100)
compteEpargne = Compte("Epargne", 34.5)
pers.ajouter_compte(compteCourant)
pers.ajouter_compte(compteEpargne)

print(pers.to_dict())