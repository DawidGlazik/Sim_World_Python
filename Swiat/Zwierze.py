from abc import abstractmethod
from Swiat.Organizm import Organizm
from Rosliny.Pole import Pole
import random


class Zwierze(Organizm):

    @abstractmethod
    def narodziny(self, x, y):
        pass

    def ruch(self, x, y):
        if isinstance(self.swiat.plansza[self.polozenie[0]+x][self.polozenie[1]+y], Pole):
            self.swiat.plansza[self.polozenie[0]+x][self.polozenie[1]+y] = self.swiat.plansza[self.polozenie[0]][self.polozenie[1]]
            self.swiat.plansza[self.polozenie[0]][self.polozenie[1]] = Pole()
            self.polozenie[0] += x
            self.polozenie[1] += y
        else:
            self.swiat.plansza[self.polozenie[0] + x][self.polozenie[1] + y].kolizja(self)

    def __init__(self, swiat=None, polozenie=None):
        self.sila = 0
        self.wiek = 0
        self.inicjatywa = 0
        self.polozenie = polozenie
        self.swiat = swiat
        self.nazwa = "Zwierze"

    def rozmnazanie(self):
        if self.polozenie[0] == 0:
            if self.polozenie[1] == 0:
                los = random.randint(0,2)
                if los == 0:
                    self.narodziny(0,1)
                elif los == 1:
                    self.narodziny(1,1)
                elif los == 2:
                    self.narodziny(1,0)
            elif self.polozenie[1] == self.swiat.szerokosc - 1:
                los = random.randint(0, 2)
                if los == 0:
                    self.narodziny(0, -1)
                elif los == 1:
                    self.narodziny(1, -1)
                elif los == 2:
                    self.narodziny(1, 0)
            else:
                los = random.randint(0, 4)
                if los == 0:
                    self.narodziny(0, -1)
                elif los == 1:
                    self.narodziny(1, -1)
                elif los == 2:
                    self.narodziny(1, 0)
                elif los == 3:
                    self.narodziny(0, 1)
                elif los == 4:
                    self.narodziny(1, 1)
        elif self.polozenie[0] == self.swiat.wysokosc - 1:
            if self.polozenie[1] == 0:
                los = random.randint(0,2)
                if los == 0:
                    self.narodziny(0,1)
                elif los == 1:
                    self.narodziny(-1,1)
                elif los == 2:
                    self.narodziny(-1,0)
            elif self.polozenie[1] == self.swiat.szerokosc - 1:
                los = random.randint(0, 2)
                if los == 0:
                    self.narodziny(0, -1)
                elif los == 1:
                    self.narodziny(-1, -1)
                elif los == 2:
                    self.narodziny(-1, 0)
            else:
                los = random.randint(0, 4)
                if los == 0:
                    self.narodziny(0, 1)
                elif los == 1:
                    self.narodziny(-1, 1)
                elif los == 2:
                    self.narodziny(-1, 0)
                elif los == 3:
                    self.narodziny(0, -1)
                elif los == 4:
                    self.narodziny(-1, -1)
        elif self.polozenie[1] == 0:
            los = random.randint(0, 4)
            if los == 0:
                self.narodziny(0, 1)
            elif los == 1:
                self.narodziny(-1, 1)
            elif los == 2:
                self.narodziny(-1, 0)
            elif los == 3:
                self.narodziny(1, 1)
            elif los == 4:
                self.narodziny(1, 0)
        elif self.polozenie[1] == self.swiat.szerokosc - 1:
            los = random.randint(0, 4)
            if los == 0:
                self.narodziny(0, -1)
            elif los == 1:
                self.narodziny(-1, -1)
            elif los == 2:
                self.narodziny(-1, 0)
            elif los == 3:
                self.narodziny(1, -1)
            elif los == 4:
                self.narodziny(1, 0)
        else:
            los = random.randint(0, 7)
            if los == 0:
                self.narodziny(0, 1)
            elif los == 1:
                self.narodziny(1, 0)
            elif los == 2:
                self.narodziny(1, 1)
            elif los == 3:
                self.narodziny(-1, 0)
            elif los == 4:
                self.narodziny(-1, 1)
            elif los == 5:
                self.narodziny(-1, -1)
            elif los == 6:
                self.narodziny(0, -1)
            elif los == 7:
                self.narodziny(1, -1)

    def akcja(self):
        if self.polozenie[0] == 0:
            if self.polozenie[1] == 0:
                los = random.randint(0, 2)
                if los == 0:
                    self.ruch(0, 1)
                elif los == 1:
                    self.ruch(1, 1)
                elif los == 2:
                    self.ruch(1, 0)
            elif self.polozenie[1] == self.swiat.szerokosc - 1:
                los = random.randint(0, 2)
                if los == 0:
                    self.ruch(0, -1)
                elif los == 1:
                    self.ruch(1, -1)
                elif los == 2:
                    self.ruch(1, 0)
            else:
                los = random.randint(0, 4)
                if los == 0:
                    self.ruch(0, -1)
                elif los == 1:
                    self.ruch(1, -1)
                elif los == 2:
                    self.ruch(1, 0)
                elif los == 3:
                    self.ruch(0, 1)
                elif los == 4:
                    self.ruch(1, 1)
        elif self.polozenie[0] == self.swiat.wysokosc - 1:
            if self.polozenie[1] == 0:
                los = random.randint(0, 2)
                if los == 0:
                    self.ruch(0, 1)
                elif los == 1:
                    self.ruch(-1, 1)
                elif los == 2:
                    self.ruch(-1, 0)
            elif self.polozenie[1] == self.swiat.szerokosc - 1:
                los = random.randint(0, 2)
                if los == 0:
                    self.ruch(0, -1)
                elif los == 1:
                    self.ruch(-1, -1)
                elif los == 2:
                    self.ruch(-1, 0)
            else:
                los = random.randint(0, 4)
                if los == 0:
                    self.ruch(0, 1)
                elif los == 1:
                    self.ruch(-1, 1)
                elif los == 2:
                    self.ruch(-1, 0)
                elif los == 3:
                    self.ruch(0, -1)
                elif los == 4:
                    self.ruch(-1, -1)
        elif self.polozenie[1] == 0:
            los = random.randint(0, 4)
            if los == 0:
                self.ruch(0, 1)
            elif los == 1:
                self.ruch(-1, 1)
            elif los == 2:
                self.ruch(-1, 0)
            elif los == 3:
                self.ruch(1, 1)
            elif los == 4:
                self.ruch(1, 0)
        elif self.polozenie[1] == self.swiat.szerokosc - 1:
            los = random.randint(0, 4)
            if los == 0:
                self.ruch(0, -1)
            elif los == 1:
                self.ruch(-1, -1)
            elif los == 2:
                self.ruch(-1, 0)
            elif los == 3:
                self.ruch(1, -1)
            elif los == 4:
                self.ruch(1, 0)
        else:
            los = random.randint(0, 7)
            if los == 0:
                self.ruch(0, 1)
            elif los == 1:
                self.ruch(1, 0)
            elif los == 2:
                self.ruch(1, 1)
            elif los == 3:
                self.ruch(-1, 0)
            elif los == 4:
                self.ruch(-1, 1)
            elif los == 5:
                self.ruch(-1, -1)
            elif los == 6:
                self.ruch(0, -1)
            elif los == 7:
                self.ruch(1, -1)

    def kolizja(self, org):
        if org.nazwa == self.nazwa:
            if org.wiek > 2:
                self.rozmnazanie()
        elif org.sila >= self.sila:
            komentarz = ""
            komentarz += str(org.nazwa)
            komentarz += str(org.polozenie)
            komentarz += " pokonuje "
            komentarz += str(self.nazwa)
            komentarz += str(self.polozenie)
            self.swiat.konsola += komentarz
            self.swiat.konsola += "\n"
            for i, organizm in enumerate(self.swiat.organizmy):
                if organizm.polozenie[0] == self.polozenie[0] and organizm.polozenie[1] == self.polozenie[1]:
                    del self.swiat.organizmy[i]
            self.swiat.plansza[self.polozenie[0]][self.polozenie[1]] = org
            self.swiat.plansza[org.polozenie[0]][org.polozenie[1]] = Pole()
            org.polozenie[0] = self.polozenie[0]
            org.polozenie[1] = self.polozenie[1]
        else:
            komentarz = ""
            komentarz += str(org.nazwa)
            komentarz += str(org.polozenie)
            komentarz += " przegrywa z "
            komentarz += str(self.nazwa)
            komentarz += str(self.polozenie)
            self.swiat.konsola += komentarz
            self.swiat.konsola += "\n"
            self.swiat.plansza[org.polozenie[0]][org.polozenie[1]] = Pole()
            for i, organizm in enumerate(self.swiat.organizmy):
                if organizm.polozenie[0] == org.polozenie[0] and organizm.polozenie[1] == org.polozenie[1]:
                    del self.swiat.organizmy[i]
