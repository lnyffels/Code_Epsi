from enum import Enum

class Formule(Enum):
    MA_HOSPI_NR = 0
    MA_ECO_NR = 1
    MA_100_NR = 2
    MA_100_R = 3
    MA_125_R = 4
    MA_150_R = 5
    MA_200_R = 6

    def __str__(self):
        if self == Formule.MA_HOSPI_NR:
            return "Ma Santé Hospi Tradi"
        elif self == Formule.MA_ECO_NR:
            return "Ma Santé Eco Tradi"
        elif self == Formule.MA_100_NR:
            return "Ma Santé 100% Tradi"
        elif self == Formule.MA_100_R:
            return "Ma Santé 100% Néo"
        elif self == Formule.MA_125_R:
            return "Ma Santé 125% Néo"
        elif self == Formule.MA_150_R:
            return "Ma Santé 150% Néo"
        elif self == Formule.MA_200_R:
            return "Ma Santé 200% Néo"
        else:
            raise Exception("Valeur en dehors de l'enumération")

    @staticmethod
    def titre_formule(valeur_option):
        if valeur_option == "MA_HOSPI_NR":
            return "Ma Santé Hospi Tradi"
        elif valeur_option == "MA_ECO_NR":
            return "Ma Santé Eco Tradi"
        elif valeur_option == "MA_100_NR":
            return "Ma Santé 100% Tradi"
        elif valeur_option == "MA_100_R":
            return "Ma Santé 100% Néo"
        elif valeur_option == "MA_125_R":
            return "Ma Santé 125% Néo"
        elif valeur_option == "MA_150_R":
            return "Ma Santé 150% Néo"
        elif valeur_option == "MA_200_R":
            return "Ma Santé 200% Néo"
        else:
            raise Exception("Valeur en dehors de l'enumération")

    @staticmethod
    def titre_prestation(valeur_option):
        if valeur_option == "APPENDICITE_CHIR":
            return "Appendicite - Honoraire Chirurgien"
        elif valeur_option == "APPENDICITE_ANES":
            return "Appendicite - Honoraire Anesthésiste"
        elif valeur_option == "ACCOUCHEMENT_OBST":
            return "Accouchement - Honoraire Obstétricien"
        elif valeur_option == "ACCOUCHEMENT_ANES":
            return "Accouchement - Honoraire Anesthésiste"
        elif valeur_option == "FORFAIT_HOSP":
            return "Forfait hospitalier - 4 jours"
        elif valeur_option == "CHAMBRE_PART":
            return "Chambre particulière - 4 jours"
        elif valeur_option == "LIT_ACCO":
            return "Lit d'accompagnement - 4 jours"
        else:
            raise Exception("Valeur en dehors de l'enumération")

