import datetime

class Operation:
    def __init__(self, montant, description, type_operation):
        self.id_operation = None
        self.montant = montant
        self.date_operation = datetime.datetime.now()
        self.description = description
        self.type_operation = type_operation


