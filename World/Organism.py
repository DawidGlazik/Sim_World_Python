from abc import ABC, abstractmethod


class Organism(ABC):

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def collision(self, org):
        pass
