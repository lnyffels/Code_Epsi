class Utilisateur:
    def __init__(self, identifiant, nom, motDePasse):
        self.identifiant = identifiant
        self.nom = nom
        self.__motDePasse = motDePasse
        self.__nom_interne = None

    def controler_mot_de_passe(self, password):
        return self.__motDePasse == password

    def __concatener_elements(self):
        self.__nom_interne = self.identifiant + "-" + self.nom


greg = Utilisateur("S611234", "Royer", "azer@ty")
greg.controler_mot_de_passe("toto")    # False
mot = greg.__motDePasse    # ERREUR : ttributeError: 'Utilisateur' object has no attribute '__motDePasse'
greg.__concatener_elements()   # ERREUR : AttributeError: 'Utilisateur' object has no attribute '__concatener_elements'