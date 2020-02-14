from Tarificateur.model.request import Request
from Tarificateur.model.response import Response
from Tarificateur.model.montant import APPENDICITE, ACCOUCHEMENT, FORFAIT
from Tarificateur.model.enum_formule import Formule


class Simulateur:

    def __init__(self, req: Request):
        self.depense = req.depenses
        self.prestation = req.prestation
        self.formule = req.formule


    def calculer_remboursements(self):
        # Cas formule AXA : Ma santé Hospi Tradi
        if self.is_hospi_tradi_and_appendicite_chirurgien():
            return self.appliquer_formule(APPENDICITE.CHIRURGIEN.MONTANT_BASE_SECU,
                                          APPENDICITE.CHIRURGIEN.MA_HOSPI_NR)

        elif self.is_hospi_tradi_and_appendicite_anesthesiste():
            return self.appliquer_formule(APPENDICITE.ANESTHESISTE.MONTANT_BASE_SECU,
                                          APPENDICITE.ANESTHESISTE.MA_HOSPI_NR)

        elif self.is_hospi_tradi_and_accouchement_anesthesiste():
            return self.appliquer_formule(ACCOUCHEMENT.ANESTHESISTE.MONTANT_BASE_SECU,
                                          ACCOUCHEMENT.ANESTHESISTE.MA_HOSPI_NR)

        elif self.is_hospi_tradi_and_accouchement_obstetricien():
            return self.appliquer_formule(ACCOUCHEMENT.OBSTETRICIEN.MONTANT_BASE_SECU,
                                          ACCOUCHEMENT.OBSTETRICIEN.MA_HOSPI_NR)

        elif self.is_hospi_tradi_and_chambre_particuliere():
            return self.appliquer_formule_forfait(FORFAIT.CHAMBRE_PARTICULIERE,
                                          FORFAIT.CHAMBRE_PARTICULIERE.MONTANT_MA_HOSPI_NR)
        # Ajout formule lit d'appoint
        else:
            raise Exception("La formule demandée n'est pas implémentée.")

    def appliquer_formule(self, montant_base_secu, taux_formule):
        res = Response()
        # US : Montant saisi inférieur au plafond sécu
        if self.depense < montant_base_secu:
           raise Exception(f"Veuillez saisir un montant entre {montant_base_secu} euros et 8000 euros")
        res.base_secu = montant_base_secu
        res.rac_avant_axa = format(self.depense - montant_base_secu, '.2f')
        montant_formule_axa = montant_base_secu * taux_formule / 100
        res.axa_plus_secu = min(self.depense, montant_formule_axa)
        res.rac_prospect = format(self.depense - res.axa_plus_secu, '.2f')
        return res

    def appliquer_formule_forfait(self, montant_base_secu, montant_forfait_formule):
        res = Response()
        res.base_secu = montant_base_secu.MONTANT_MA_HOSPI_NR
        res.rac_avant_axa = format(self.depense - res.base_secu, '.2f')
        montant_formule_axa = montant_forfait_formule * 4                   # US: Changement durée de forfait passer à 6 j
        res.axa_plus_secu = min(self.depense, montant_formule_axa)
        res.rac_prospect = format(self.depense - res.axa_plus_secu, '.2f')
        return res


    def is_hospi_tradi_and_appendicite_chirurgien(self):
        return self.formule == Formule.MA_HOSPI_NR.name and self.prestation == APPENDICITE.CHIRURGIEN.PRESTATION

    def is_hospi_tradi_and_appendicite_anesthesiste(self):
        return self.formule == Formule.MA_HOSPI_NR.name and self.prestation == APPENDICITE.ANESTHESISTE.PRESTATION

    def is_hospi_tradi_and_accouchement_obstetricien(self):
        return self.formule == Formule.MA_HOSPI_NR.name and self.prestation == ACCOUCHEMENT.OBSTETRICIEN.PRESTATION

    def is_hospi_tradi_and_accouchement_anesthesiste(self):
        return self.formule == Formule.MA_HOSPI_NR.name and self.prestation == ACCOUCHEMENT.ANESTHESISTE.PRESTATION

    def is_hospi_tradi_and_chambre_particuliere(self):
        return self.formule == Formule.MA_HOSPI_NR.name and self.prestation == FORFAIT.CHAMBRE_PARTICULIERE.PRESTATION

    def is_hospi_tradi_and_lit_accompagnement(self):
        return self.formule == Formule.MA_HOSPI_NR.name and self.prestation == FORFAIT.LIT_ACCOMPAGNEMENT.PRESTATION
