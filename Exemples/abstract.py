import abc


class Vehicule(abc.ABC):
    @abc.abstractmethod
    def avancer(self):
        pass


class Voiture(Vehicule):
    def __init__(self):
        self.reservoir = 40

    def avancer(self):
        self.reservoir -= 1


car = Voiture()
car.avancer()
# v= Vehicule()
print(car.reservoir)
