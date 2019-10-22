class Intervention:
    def __init__(self, code, ref_client, piece, probleme):
        self.code = code
        self.ref_client = ref_client
        self.piece = piece
        self.probleme = probleme

    @classmethod
    def from_dict(cls, dict):
        return cls(
            code=dict["code"],
            ref_client=dict["ref_client"],
            piece=dict["piece"],
            probleme=dict["probleme"]
        )

    def to_dict(self):
        return {
            "code" : self.code,
            "ref_client" : self.ref_client,
            "piece" : self.piece,
            "probleme" : self.probleme
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

    def __str__(self):
        return f"== Intervention == \n" \
               f"Code : {self.code} \n" \
               f"Référence Client : {self.ref_client} \n" \
               f"Pièce à diagnostiquer : {self.piece} \n" \
               f"Panne : {self.probleme} \n" \
