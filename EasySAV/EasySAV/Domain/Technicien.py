from EasySAV.EasySAV.Domain.Intervention import Intervention
from typing import List

class Technicien(object):

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.interventions: List[Intervention] = list()

    def ajouter_intervention(self, intervention: Intervention):
        self.interventions.append(intervention)

