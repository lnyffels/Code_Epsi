import pytest
import uuid
from unittest import mock

from EasySAV.EasySAV.Domain.Intervention import Intervention
from EasySAV.EasySAV.Use_cases.Intervention_list_use_case import InterventionUseCase

@pytest.fixture()
def domain_interventions():
    interv1 = Intervention(
        code=uuid.uuid4(),
        ref_client = "ISJSJK",
        piece="TV",
        probleme="Ecran noir"
    )
    interv2 = Intervention(
        code=uuid.uuid4(),
        ref_client="TYFFRS",
        piece="Lave vaisselle",
        probleme="Fuite"
    )
    interv3 = Intervention(
        code=uuid.uuid4(),
        ref_client="AZEZEE",
        piece="Plaques four",
        probleme="Allumage"
    )
    interv4 = Intervention(
        code=uuid.uuid4(),
        ref_client="TFTGRS",
        piece="Ordinateur",
        probleme="Ecran bleu au démarrage"
    )
    return [interv1, interv2, interv3, interv4]

def test_intervention_liste_sans_parametre(domain_interventions):
    repo = mock.Mock()
    repo.list.return_value = domain_interventions

    intervention_list_uc = InterventionUseCase(repo)
    result = intervention_list_uc.execute()

    repo.list.assert_called_with()
    assert result == domain_interventions