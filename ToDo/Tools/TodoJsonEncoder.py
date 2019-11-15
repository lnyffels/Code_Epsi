import json

class TodoJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = {
                'description': str(o.description),
                'status': o.status.name
            }
            return to_serialize
        except AttributeError:
            return super().default(o)