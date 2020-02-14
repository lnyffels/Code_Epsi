from enum import Enum

class TypeOperation(Enum):
    CREDIT = 0
    DEBIT = 1

    def __str__(self):
        if self == TypeOperation.CREDIT:
            return "C"
        elif self == TypeOperation.DEBIT:
            return "D"
        else:
            raise Exception("Valeur en dehors de l'enumération")
