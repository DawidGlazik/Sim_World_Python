from Swiat.Zwierze import Zwierze
from Rosliny.Pole import Pole


class Czlowiek(Zwierze):

    def __init__(self, swiat=None, polozenie=None, sila=5, wiek=0, trwanie=5, przerwa=0):
        self.sila = sila
        self.inicjatywa = 4
        self.wiek = wiek
        self.swiat = swiat
        self.polozenie = polozenie
        self.trwanie = trwanie
        self.przerwa = przerwa
        self.nazwa = "Czlowiek"

    def sprawdzIZabij(self, x, y):
        if not isinstance(self.swiat.plansza[self.polozenie[0] + x][self.polozenie[1] + y], Pole):
            komentarz = ""
            komentarz += self.swiat.plansza[self.polozenie[0] + x][self.polozenie[1] + y].nazwa
            komentarz += self.swiat.plansza[self.polozenie[0] + x][self.polozenie[1] + y].polozenie
            komentarz += " zabity(a) przez (calopalenie) "
            komentarz += self.nazwa
            komentarz += self.polozenie
            self.swiat.konsola += komentarz
            self.swiat.plansza[self.polozenie[0] + x][self.polozenie[1] + y] = Pole()
            for i, organizm in enumerate(self.swiat.organizmy):
                if organizm.polozenie[0] == self.polozenie[0] + x and organizm.polozenie[1] == self.polozenie[1] + y:
                    del self.swiat.organizmy[i]

    def akcja(self, kierunek):
        if kierunek == 0:
            return
        elif kierunek == 1:
            if self.polozenie[0] == 0:
                return
            else:
                if isinstance(self.swiat.plansza[self.polozenie[0] - 1][self.polozenie[1]], Pole):
                    self.swiat.plansza[self.polozenie[0] - 1][self.polozenie[1]] = \
                    self.swiat.plansza[self.polozenie[0]][self.polozenie[1]]
                    self.swiat.plansza[self.polozenie[0]][self.polozenie[1]] = Pole()
                    self.polozenie[0] -= 1
                else:
                    self.swiat.plansza[self.polozenie[0] - 1][self.polozenie[1]].kolizja(self)
        elif kierunek == 2:
            if self.polozenie[0] == self.swiat.wysokosc - 1:
                return
            else:
                if isinstance(self.swiat.plansza[self.polozenie[0] + 1][self.polozenie[1]], Pole):
                    self.swiat.plansza[self.polozenie[0] + 1][self.polozenie[1]] = \
                    self.swiat.plansza[self.polozenie[0]][self.polozenie[1]]
                    self.swiat.plansza[self.polozenie[0]][self.polozenie[1]] = Pole()
                    self.polozenie[0] += 1
                else:
                    self.swiat.plansza[self.polozenie[0] + 1][self.polozenie[1]].kolizja(self)
        elif kierunek == 3:
            if self.polozenie[1] == 0:
                return
            else:
                if isinstance(self.swiat.plansza[self.polozenie[0]][self.polozenie[1] - 1], Pole):
                    self.swiat.plansza[self.polozenie[0]][self.polozenie[1] - 1] = \
                    self.swiat.plansza[self.polozenie[0]][self.polozenie[1]]
                    self.swiat.plansza[self.polozenie[0]][self.polozenie[1]] = Pole()
                    self.polozenie[1] -= 1
                else:
                    self.swiat.plansza[self.polozenie[0]][self.polozenie[1] - 1].kolizja(self)
        elif kierunek == 4:
            if self.polozenie[1] == self.swiat.szerokosc - 1:
                return
            else:
                if isinstance(self.swiat.plansza[self.polozenie[0]][self.polozenie[1] + 1], Pole):
                    self.swiat.plansza[self.polozenie[0]][self.polozenie[1] + 1] = \
                    self.swiat.plansza[self.polozenie[0]][self.polozenie[1]]
                    self.swiat.plansza[self.polozenie[0]][self.polozenie[1]] = Pole()
                    self.polozenie[1] += 1
                else:
                    self.swiat.plansza[self.polozenie[0]][self.polozenie[1] + 1].kolizja(self)

    def calopalenie(self):
        self.trwanie -= 1
        if self.polozenie[0] == 0:
            if self.polozenie[1] == 0:
                self.sprawdzIZabij(0, 1)
                self.sprawdzIZabij(1, 1)
                self.sprawdzIZabij(1, 0)
            elif self.polozenie[1] == self.swiat.szerokosc - 1:
                self.sprawdzIZabij(0, -1)
                self.sprawdzIZabij(1, -1)
                self.sprawdzIZabij(1, 0)
            else:
                self.sprawdzIZabij(0, -1)
                self.sprawdzIZabij(1, -1)
                self.sprawdzIZabij(1, 0)
                self.sprawdzIZabij(0, 1)
                self.sprawdzIZabij(1, 1)
        elif self.polozenie[0] == self.swiat.wysokosc - 1:
            if self.polozenie[1] == 0:
                self.sprawdzIZabij(0, 1)
                self.sprawdzIZabij(-1, 1)
                self.sprawdzIZabij(-1, 0)
            elif self.polozenie[1] == self.swiat.szerokosc - 1:
                self.sprawdzIZabij(0, -1)
                self.sprawdzIZabij(-1, -1)
                self.sprawdzIZabij(-1, 0)
            else:
                self.sprawdzIZabij(0, 1)
                self.sprawdzIZabij(-1, 1)
                self.sprawdzIZabij(-1, 0)
                self.sprawdzIZabij(0, -1)
                self.sprawdzIZabij(-1, -1)
        elif self.polozenie[1] == 0:
            self.sprawdzIZabij(0, 1)
            self.sprawdzIZabij(-1, 1)
            self.sprawdzIZabij(-1, 0)
            self.sprawdzIZabij(1, 1)
            self.sprawdzIZabij(1, 0)
        elif self.polozenie[1] == self.swiat.szerokosc - 1:
            self.sprawdzIZabij(0, -1)
            self.sprawdzIZabij(-1, -1)
            self.sprawdzIZabij(-1, 0)
            self.sprawdzIZabij(1, -1)
            self.sprawdzIZabij(1, 0)
        else:
            self.sprawdzIZabij(0, 1)
            self.sprawdzIZabij(1, 0)
            self.sprawdzIZabij(1, 1)
            self.sprawdzIZabij(-1, 0)
            self.sprawdzIZabij(-1, 1)
            self.sprawdzIZabij(-1, -1)
            self.sprawdzIZabij(0, -1)
            self.sprawdzIZabij(1, -1)

        def narodziny(self, x, y):
            pass