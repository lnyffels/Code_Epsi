from EasySAV.EasySAV.Domain.Intervention import Intervention

class InterventionSaveUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, interv_to_save):
        inter = Intervention.from_dict(interv_to_save)
        return self.repo.save(inter)