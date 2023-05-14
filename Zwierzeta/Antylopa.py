from Swiat.Zwierze import Zwierze
from Rosliny.Pole import Pole
import random

class Antylopa(Zwierze):

    def __init__(self, swiat=None, polozenie=None, sila=4, wiek=0):
        super().__init__()
        self.swiat = swiat
        self.polozenie = polozenie
        self.inicjatywa = 4
        self.sila = sila
        self.wiek = wiek
        self.nazwa = "Antylopa"

    def narodziny(self, x, y):
        if isinstance(self.swiat.plansza[self.polozenie[0] + x][self.polozenie[1] + y], Pole):
            komentarz = ""
            komentarz += "Narodziny organizmu: "
            komentarz += self.nazwa
            komentarz += "("
            komentarz += self.polozenie[0] + x + 1
            komentarz += ","
            komentarz += self.polozenie[1] + y + 1
            komentarz += ")"
            self.swiat.konsola += komentarz
            self.swiat.dodajOrganizm(Antylopa(self.swiat, (self.polozenie[0] + x, self.polozenie[1] + y)))

    def akcja(self):
        if self.polozenie[0] == 0:
            if self.polozenie[1] == 0:
                los = random.randint(0, 4)
                if los == 0:
                    self.ruch(0, 1)
                elif los == 1:
                    self.ruch(1, 1)
                elif los == 2:
                    self.ruch(1, 0)
                elif los == 3:
                    self.ruch(0, 2)
                elif los == 4:
                    self.ruch(2, 0)
            elif self.polozenie[1] == self.swiat.szerokosc - 1:
                los = random.randint(0, 4)
                if los == 0:
                    self.ruch(0, -1)
                elif los == 1:
                    self.ruch(1, -1)
                elif los == 2:
                    self.ruch(1, 0)
                elif los == 3:
                    self.ruch(0, -2)
                elif los == 4:
                    self.ruch(2, 0)
            else:
                los = random.randint(0, 7)
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
                elif los == 5 and self.polozenie[1] != self.swiat.szerokosc - 2:
                    self.ruch(0, 2)
                elif los == 6 and self.polozenie[0] != self.swiat.wysokosc - 2:
                    self.ruch(2, 0)
                elif los == 7 and  self.polozenie[1] != 1:
                    self.ruch(0, -2)
        elif self.polozenie[0] == self.swiat.wysokosc - 1:
            if self.polozenie[1] == 0:
                los = random.randint(0, 4)
                if los == 0:
                    self.ruch(0, 1)
                elif los == 1:
                    self.ruch(-1, 1)
                elif los == 2:
                    self.ruch(-1, 0)
                elif los == 3:
                    self.ruch(-2, 0)
                elif los == 4:
                    self.ruch(0, 2)
            elif self.polozenie[1] == self.swiat.szerokosc - 1:
                los = random.randint(0, 4)
                if los == 0:
                    self.ruch(0, -1)
                elif los == 1:
                    self.ruch(-1, -1)
                elif los == 2:
                    self.ruch(-1, 0)
                elif los == 3:
                    self.ruch(-2, 0)
                elif los == 4:
                    self.ruch(0, -2)
            else:
                los = random.randint(0, 7)
                if los == 0:
                    self.ruch(0, -1)
                elif los == 1:
                    self.ruch(-1, 1)
                elif los == 2:
                    self.ruch(-1, 0)
                elif los == 3:
                    self.ruch(0, -1)
                elif los == 4:
                    self.ruch(-1, -1)
                elif los == 5 and self.polozenie[1] != self.swiat.szerokosc - 2:
                    self.ruch(0, 2)
                elif los == 6 and self.polozenie[0] != 1:
                    self.ruch(-2, 0)
                elif los == 7 and self.polozenie[1] != 1:
                    self.ruch(0, -2)
        elif self.polozenie[1] == 0:
            los = random.randint(0, 7)
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
            elif los == 5:
                self.ruch(0, 2)
            elif los == 6 and self.polozenie[0] != 1:
                self.ruch(-2, 0)
            elif los == 7 and self.polozenie[0] != self.swiat.wysokosc - 2:
                self.ruch(2, 0)
        elif self.polozenie[1] == self.swiat.szerokosc - 1:
            los = random.randint(0, 7)
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
            elif los == 5:
                self.ruch(0, -2)
            elif los == 6 and self.polozenie[0] != 1:
                self.ruch(-2, 0)
            elif los == 7 and self.polozenie[0] != self.swiat.wysokosc - 2:
                self.ruch(2, 0)
        else:
            los = random.randint(0, 11)
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
            elif los == 8 and self.polozenie[0] != 1:
                self.ruch(-2, 0)
            elif los == 9 and self.polozenie[0] != self.swiat.wysokosc -2:
                self.ruch(2, 0)
            elif los == 10 and self.polozenie[1] != self.swiat.szerokosc -2:
                self.ruch(0, 2)
            elif los == 11 and self.polozenie[1] != 1:
                self.ruch(0, -2)

    def kolizja(self, org):
        szansa = random.randint(0,1)
        if isinstance(org, Antylopa):
            if self.wiek > 2:
                self.rozmnazanie()
        elif szansa == 0:
            komentarz = ""
            komentarz += self.nazwa
            komentarz += self.polozenie
            komentarz += " ucieka"
            self.swiat.konsola += komentarz
            self.swiat.konsola += "\n"
            if self.polozenie[1] != self.swiat.szerokosc - 1 and isinstance(self.swiat.plansza[self.polozenie[0][self.polozenie[1] + 1]], Pole):
                self.swiat.plansza[self.polozenie[0]][self.polozenie[1] + 1] = self.swiat.plansza[self.polozenie[0]][self.polozenie[1]]
                self.swiat.plansza[self.polozenie[0]][self.polozenie[1]] = Pole()
                self.polozenie[1] += 1
            elif self.polozenie[0] != self.swiat.wysokosc - 1 and isinstance(self.swiat.plansza[self.polozenie[0] + 1][self.polozenie[1]], Pole):
                self.swiat.plansza[self.polozenie[0] + 1][self.polozenie[1]] = self.swiat.plansza[self.polozenie[0]][self.polozenie[1]]
                self.swiat.plansza[self.polozenie[0]][self.polozenie[1]] = Pole()
                self.polozenie[0] += 1
            elif self.polozenie[1] != 0 and isinstance(self.swiat.plansza[self.polozenie[0]][self.polozenie[1] - 1], Pole):
                self.swiat.plansza[self.polozenie[0]][self.polozenie[1] - 1] = self.swiat.plansza[self.polozenie[0]][self.polozenie[1]]
                self.swiat.plansza[self.polozenie[0]][self.polozenie[1]] = Pole()
                self.polozenie[1] -= 1
            elif self.polozenie[0] != 0 and isinstance(self.swiat.plansza[self.polozenie[0] - 1][self.polozenie[1]], Pole):
                self.swiat.plansza[self.polozenie[0] - 1][self.polozenie[1]] = self.swiat.plansza[self.polozenie[0]][self.polozenie[1]]
                self.swiat.plansza[self.polozenie[0]][self.polozenie[1]] = Pole()
                self.polozenie[0] -= 1
        elif org.sila > self.sila:
            komentarz = ""
            komentarz += org.nazwa
            komentarz += org.polozenie
            komentarz += " pokonuje "
            komentarz += self.nazwa
            komentarz += self.polozenie
            self.swiat.konsola += komentarz
            for i, organizm in enumerate(self.swiat.organizmy):
                if organizm.polozenie[0] == self.polozenie[0] and organizm.polozenie[1] == self.polozenie[1]:
                    del self.swiat.organizmy[i]
            self.swiat.plansza[self.polozenie[0]][self.polozenie[1]] = org
            self.swiat.plansza[org.polozenie[0]][org.polozenie[1]] = Pole()
            org.polozenie[0] = self.polozenie[0]
            org.polozenie[1] = self.polozenie[1]
        else:
            komentarz = ""
            komentarz += org.nazwa
            komentarz += org.polozenie
            komentarz += " przegrywa z "
            komentarz += self.nazwa
            komentarz += self.polozenie
            self.swiat.konsola += komentarz
            self.swiat.plansza[org.polozenie[0]][org.polozenie[1]] = Pole()
            for i, organizm in enumerate(self.swiat.organizmy):
                if organizm.polozenie[0] == self.polozenie[0] and organizm.polozenie[1] == self.polozenie[1]:
                    del self.swiat.organizmy[i]
