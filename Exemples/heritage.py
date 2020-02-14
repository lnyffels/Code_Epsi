class Personne:
    def __init__(self, nom, age=18):
        self._nom = nom
        self._age = age

    def _is_adulte(self):
        return self._age >= 18

class Invite(Personne):
    def __init__(self, nom, age, entreprise):
        super().__init__(nom, age)
        self.entreprise = entreprise

    def _is_adulte(self):
        return self._age >= 21

    def __str__(self):
        if self._is_adulte():
            return f"GUEST : {self._nom}, âge: {self._age}, Entreprise : {self.entreprise}"
        else:
            return "invité mineur"

guest = Invite("Dupont", 14, "AXA")
print(guest)
