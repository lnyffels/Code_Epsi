import uuid

class Personne:

    friends = []

    def __init__(self, nom):
       self.nom = nom


    @classmethod
    def ajouter_ami(cls, ami):
        cls.friends.append(ami) # Accès juste aux proprité

    @staticmethod
    def generer_uuid():
        # pas d'accès aux méthodes et propriétés de la classe ou instance
        return str(uuid.uuid4())

pers = Personne("lnf")
Personne.ajouter_ami("bob")
guid1 = Personne.generer_uuid()
print(guid1)