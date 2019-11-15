from EasySAV.EasySAV.Domain.Intervention import Intervention
from typing import List

class Technicien(object):

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.interventions: List[Intervention] = list()

    def ajouter_intervention(self, intervention: Intervention):
        self.interventions.append(intervention)


interv1 = Intervention(233,"azze", "azerttt", "jjjjjjj")
interv2 = Intervention(566,"juju", "asdt", "aaaaa")
tech = Technicien("lnf", "bob")
tech.ajouter_intervention(interv1)
tech.ajouter_intervention(interv2)
for i in tech.interventions:
    print(i)