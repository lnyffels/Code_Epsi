from typing import Dict


from EasySAV.EasySAV.Use_cases.Intervention_list_use_case import *
from EasySAV.EasySAV.Repository.Memrepo import *

# Alimentation de la base de données en mémoire
intervention1 = {
            "code": "d753578e-tc0f-4e75-81b8-566c5dfda35b",
            "ref_client" : "CFGRRF",
            "piece" : "lave linge",
            "probleme" : "fuite"
 }

intervention2 = {
            "code": "e987578e-fc0v-5e75-82b8-566c5dfda66y",
            "ref_client": "REFTY",
            "piece": "TV",
            "probleme": "allumage"
}

intervention3 = {
            "code": "j953979d-uc4f-5e75-81b8-576G5dfda75p",
            "ref_client": "YGTGDR",
            "piece": "lave vaisselle",
            "probleme": "fuite"
}


repo = MemRepo([intervention1, intervention2, intervention3])
use_case = InterventionUseCase(repo)
liste_interventions = use_case.execute()

for i in liste_interventions:
    print(i)