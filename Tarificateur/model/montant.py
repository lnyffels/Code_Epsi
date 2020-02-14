class APPENDICITE:
    class CHIRURGIEN:
        MONTANT_BASE_SECU = 187.89
        MA_HOSPI_NR = 400    # en %
        MA_ECO_NR = 100
        MA_100_NR = 100
        MA_100_R = 100
        MA_125_R = 145
        MA_150_R = 170
        MA_200_NR = 220
        PRESTATION = "APPENDICITE_CHIR"

    class ANESTHESISTE:
        MONTANT_BASE_SECU = 103.64
        MA_HOSPI_NR = 400
        MA_ECO_NR = 100
        MA_100_NR = 100
        MA_100_R = 100
        MA_125_R = 145
        MA_150_R = 170
        MA_200_NR = 220
        PRESTATION = "APPENDICITE_ANES"

class ACCOUCHEMENT:
    class OBSTETRICIEN:
        MONTANT_BASE_SECU = 313.50
        MA_HOSPI_NR = 400
        MA_ECO_NR = 100
        MA_100_NR = 100
        MA_100_R = 100
        MA_125_R = 145
        MA_150_R = 170
        MA_200_NR = 220
        PRESTATION = "ACCOUCHEMENT_OBST"

    class ANESTHESISTE:
        MONTANT_BASE_SECU = 209
        MA_HOSPI_NR = 400
        MA_ECO_NR = 100
        MA_100_NR = 100
        MA_100_R = 100
        MA_125_R = 145
        MA_150_R = 170
        MA_200_NR = 220
        PRESTATION = "ACCOUCHEMENT_ANES"

class FORFAIT:

    class CHAMBRE_PARTICULIERE:
        MONTANT_BASE_SECU = 0
        MONTANT_MA_HOSPI_NR = 90   # euros / jour
        MONTANT_MA_ECO_NR = 0
        MONTANT_MA_100_NR = 0
        MONTANT_MA_100_R = 0
        MONTANT_MA_125_R = 60
        MONTANT_MA_150_R = 70
        MONTANT_MA_200_NR = 90
        PRESTATION = "CHAMBRE_PART"

    class LIT_ACCOMPAGNEMENT:
        MONTANT_BASE_SECU = 0
        MONTANT_MA_HOSPI_NR = 15
        MONTANT_MA_ECO_NR = 0
        MONTANT_MA_100_NR = 0
        MONTANT_MA_100_R = 0
        MONTANT_MA_125_R = 15
        MONTANT_MA_150_R = 15
        MONTANT_MA_200_NR = 15
        PRESTATION = "LIT_ACCO"

