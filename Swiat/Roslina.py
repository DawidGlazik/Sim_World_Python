from abc import abstractmethod
from Rosliny import Pole
from Swiat.Organizm import Organizm
import random


class Roslina(Organizm):

    @abstractmethod
    def sprawdzIZasiej(self, x, y):
        pass

    def __init__(self, swiat=None, polozenie=None):
        self.sila = 0
        self.wiek = 0
        self.inicjatywa = 0
        self.polozenie = polozenie
        self.swiat = swiat
        self.nazwa = "Roslina"

    def akcja(self):
        los1 = random.randint(0, 14)
        if los1 != 0:
            return
        if self.polozenie[0] == 0:
            los2 = random.randint(0, 10)
            if self.polozenie[1] == 0:
                if los2 == 0:
                    self.sprawdzIZasiej(0, 1)
                elif los2 == 1:
                    self.sprawdzIZasiej(1, 1)
                elif los2 == 2:
                    self.sprawdzIZasiej(1, 0)
            elif self.polozenie[1] == self.swiat.szerokosc - 1:
                if los2 == 3:
                    self.sprawdzIZasiej(0, -1)
                elif los2 == 4:
                    self.sprawdzIZasiej(1, -1)
                elif los2 == 5:
                    self.sprawdzIZasiej(1, 0)
            else:
                if los2 == 6:
                    self.sprawdzIZasiej(0, -1)
                elif los2 == 7:
                    self.sprawdzIZasiej(1, -1)
                elif los2 == 8:
                    self.sprawdzIZasiej(1, 0)
                elif los2 == 9:
                    self.sprawdzIZasiej(0, 1)
                elif los2 == 10:
                    self.sprawdzIZasiej(1, 1)
        elif self.polozenie[0] == self.swiat.wysokosc - 1:
            los2 = random.randint(0, 10)
            if self.polozenie[1] == 0:
                if los2 == 0:
                    self.sprawdzIZasiej(0, 1)
                elif los2 == 1:
                    self.sprawdzIZasiej(-1, 1)
                elif los2 == 2:
                    self.sprawdzIZasiej(-1, 0)
            elif self.polozenie[1] == self.swiat.szerokosc - 1:
                if los2 == 3:
                    self.sprawdzIZasiej(0, -1)
                elif los2 == 4:
                    self.sprawdzIZasiej(-1, -1)
                elif los2 == 5:
                    self.sprawdzIZasiej(-1, 0)
            else:
                if los2 == 6:
                    self.sprawdzIZasiej(0, 1)
                elif los2 == 7:
                    self.sprawdzIZasiej(-1, 1)
                elif los2 == 8:
                    self.sprawdzIZasiej(-1, 0)
                elif los2 == 9:
                    self.sprawdzIZasiej(0, -1)
                elif los2 == 10:
                    self.sprawdzIZasiej(-1, -1)
        elif self.polozenie[0] == self.swiat.wysokosc - 1:
            los2 = random.randint(0, 10)
            if self.polozenie[1] == 0:
                if los2 == 0:
                    self.sprawdzIZasiej(0, 1)
                elif los2 == 1:
                    self.sprawdzIZasiej(-1, 1)
                elif los2 == 2:
                    self.sprawdzIZasiej(-1, 0)
            elif self.polozenie[1] == self.swiat.szerokosc - 1:
                if los2 == 3:
                    self.sprawdzIZasiej(0, -1)
                elif los2 == 4:
                    self.sprawdzIZasiej(-1, -1)
                elif los2 == 5:
                    self.sprawdzIZasiej(-1, 0)
            else:
                if los2 == 6:
                    self.sprawdzIZasiej(0, 1)
                elif los2 == 7:
                    self.sprawdzIZasiej(-1, 1)
                elif los2 == 8:
                    self.sprawdzIZasiej(-1, 0)
                elif los2 == 9:
                    self.sprawdzIZasiej(0, -1)
                elif los2 == 10:
                    self.sprawdzIZasiej(-1, -1)
        elif self.polozenie[1] == 0:
            los2 = random.randint(0, 4)
            if los2 == 0:
                self.sprawdzIZasiej(0, 1)
            elif los2 == 1:
                self.sprawdzIZasiej(-1, 1)
            elif los2 == 2:
                self.sprawdzIZasiej(-1, 0)
            elif los2 == 3:
                self.sprawdzIZasiej(1, 1)
            elif los2 == 4:
                self.sprawdzIZasiej(1, 0)
        elif self.polozenie[1] == self.swiat.szerokosc - 1:
            los2 = random.randint(0, 4)
            if los2 == 0:
                self.sprawdzIZasiej(0, -1)
            elif los2 == 1:
                self.sprawdzIZasiej(-1, -1)
            elif los2 == 2:
                self.sprawdzIZasiej(-1, 0)
            elif los2 == 3:
                self.sprawdzIZasiej(1, -1)
            elif los2 == 4:
                self.sprawdzIZasiej(1, 0)
        else:
            los2 = random.randint(0, 7)
            if los2 == 0:
                self.sprawdzIZasiej(0, 1)
            elif los2 == 1:
                self.sprawdzIZasiej(1, 0)
            elif los2 == 2:
                self.sprawdzIZasiej(1, 1)
            elif los2 == 3:
                self.sprawdzIZasiej(-1, 0)
            elif los2 == 4:
                self.sprawdzIZasiej(-1, 1)
            elif los2 == 5:
                self.sprawdzIZasiej(-1, -1)
            elif los2 == 6:
                self.sprawdzIZasiej(0, -1)
            elif los2 == 7:
                self.sprawdzIZasiej(1, -1)

    def kolizja(self, org):
        komentarz = ""
        komentarz += org.nazwa
        komentarz += org.polozenie
        komentarz += " zjada "
        komentarz += self.nazwa
        komentarz += self.polozenie
        self.swiat.konsola += komentarz
        self.swiat.konsola += "\n"
        for i, organizm in enumerate(self.swiat.organizmy):
            if organizm.polozenie[0] == self.polozenie[0] and organizm.polozenie[1] == self.polozenie[1]:
                del self.swiat.organizmy[i]
        self.swiat.plansza[self.polozenie[0]][self.polozenie[1]] = org
        self.swiat.plansza[org.polozenie[0]][org.polozenie[1]] = Pole.Pole()
        org.polozenie[0] = self.polozenie[0]
        org.polozenie[1] = self.polozenie[1]
