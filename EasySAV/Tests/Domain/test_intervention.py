import uuid
from EasySAV.EasySAV.Domain.Intervention import Intervention

def test_intervention_model_init():
    code = uuid.uuid4()
    intervention = Intervention(code=code, ref_client="IA42", piece="Lave linge", probleme="fuite")
    assert intervention.code == code
    assert intervention.ref_client == "IA42"
    assert intervention.piece == "Lave linge"
    assert intervention.probleme == "fuite"

def test_intervention_model_from_dict():
    code = uuid.uuid4()
    intervention = Intervention.from_dict(
        {
            'code' : code,
            'ref_client' : "IA42",
            'piece' : "Lave linge",
            'probleme' : "fuite"
        }
    )
    assert intervention.code == code
    assert intervention.ref_client == "IA42"
    assert intervention.piece == "Lave linge"
    assert intervention.probleme == "fuite"


def test_intervention_model_to_dict():
    code = uuid.uuid4()
    dico_intervention = {
            'code' : code,
            'ref_client' : "IA42",
            'piece' : "Lave linge",
            'probleme' : "fuite"
        }

    intervention = Intervention.from_dict(dico_intervention)
    assert intervention.to_dict() == dico_intervention


def test_intervention_model_comparaison():
    dico_intervention = {
        'code': uuid.uuid4(),
        'ref_client': "IA42",
        'piece': "Lave linge",
        'probleme': "fuite"
    }

    intervention1 = Intervention.from_dict(dico_intervention)
    intervention2 = Intervention.from_dict(dico_intervention)
    assert intervention1 == intervention2