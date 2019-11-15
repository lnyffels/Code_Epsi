import json


class InterventionJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = {
                'code': str(o.code),
                'ref_client': o.ref_client,
                'piece': o.piece,
                'probleme': o.probleme
            }
            return to_serialize
        except AttributeError:
            return super().default(o)