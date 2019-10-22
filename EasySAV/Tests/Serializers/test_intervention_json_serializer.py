import json
import uuid
from EasySAV.EasySAV.Serializers.intervention_json_serializer import InterventionJsonEncoder
from EasySAV.EasySAV.Domain.Intervention import Intervention

def test_serialize_domain_intervention():
    code = uuid.uuid4()
    intervention = Intervention(
            code =code,
            ref_client="IA42",
            piece= "Lave linge",
            probleme= "fuite"
    )

    expected_intervention_json = """
            {{
            "code": "{}",
            "ref_client": "IA42",
            "piece": "Lave linge",
            "probleme": "fuite"
            }}
    """.format(code)
    # serialize l'objet intervention en json
    json_intervention = json.dumps(intervention, cls=InterventionJsonEncoder)
    # désérialise le flux json et compare les 2 objets
    assert json.loads(json_intervention) == json.loads(expected_intervention_json)