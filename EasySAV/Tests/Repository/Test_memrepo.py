import pytest

from EasySAV.EasySAV.Domain.Intervention import Intervention
from EasySAV.EasySAV.Repository.Memrepo import MemRepo

@pytest.fixture
def interventions_dicts():
    return [
        {
            "code": "d753578e-tc0f-4e75-81b8-566c5dfda35b",
            "ref_client" : "CFGRRF",
            "piece" : "lave linge",
            "probleme" : "fuite"
        },
        {
            "code": "e987578e-fc0v-5e75-82b8-566c5dfda66y",
            "ref_client": "REFTY",
            "piece": "TV",
            "probleme": "allumage"
        },
        {
            "code": "j953979d-uc4f-5e75-81b8-576G5dfda75p",
            "ref_client": "YGTGDR",
            "piece": "lave vaisselle",
            "probleme": "fuite"
        },
        {
            "code": "j557576e-uj7f-7e95-31h9-962c2dfda23m",
            "ref_client": "LOKIU",
            "piece": "four",
            "probleme": "résistance"
        }
    ]

def test_repository_list_sans_parametre(interventions_dicts):
    repo = MemRepo(interventions_dicts)
    interventions = [Intervention.from_dict(i) for i in interventions_dicts]

    assert repo.list() == interventions
