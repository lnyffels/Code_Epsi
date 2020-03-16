from EasySAV.EasySAV.Domain.Intervention import Intervention

class MemRepo:
    def __init__(self, data):
        self.data = data

    def get_all_interventions(self):
        return [Intervention.from_dict(i) for i in self.data]