from abc import ABC, abstractmethod


class Organizm(ABC):

    @abstractmethod
    def akcja(self):
        pass

    @abstractmethod
    def kolizja(self, org):
        pass
