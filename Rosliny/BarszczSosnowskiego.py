from Swiat.Roslina import Roslina
from Rosliny.Pole import Pole
from Swiat.Zwierze import Zwierze
from Zwierzeta.CyberOwca import CyberOwca

class BarszczSosnowskiego(Roslina):

    def __init__(self, swiat=None, polozenie=None, wiek=0):
        super().__init__()
        self.swiat = swiat
        self.polozenie = polozenie
        self.sila = 10
        self.wiek = wiek
        self.nazwa = "BarszczSosnowskiego"

    def sprawdzIZasiej(self, x, y):
        if isinstance(self.swiat.plansza[self.polozenie[0] + x][self.polozenie[1] + y], Pole):
            komentarz = ""
            komentarz += "Zasiano "
            komentarz += str(self.nazwa)
            komentarz += "("
            komentarz += str(self.polozenie[0] + x + 1)
            komentarz += ","
            komentarz += str(self.polozenie[1] + y + 1)
            komentarz += ")"
            self.swiat.konsola += komentarz
            self.swiat.konsola += "\n"
            self.swiat.dodajOrganizm(BarszczSosnowskiego(self.swiat, (self.polozenie[0] + x, self.polozenie[1] + y)))

    def sprawdzIZabij(self, x, y):
        if isinstance(self.swiat.plansza[self.polozenie[0] + x][self.polozenie[1] + y], Zwierze):
            if isinstance(self.swiat.plansza[self.polozenie[0] + x][self.polozenie[1] + y], CyberOwca):
                return
            else:
                komentarz = ""
                komentarz += str(self.swiat.plansza[self.polozenie[0] + x][self.polozenie[1] + y].nazwa)
                komentarz += str(self.swiat.plansza[self.polozenie[0] + x][self.polozenie[1] + y].polozenie)
                komentarz += " zabity(a) przez "
                komentarz += str(self.nazwa)
                komentarz += str(self.polozenie)
                self.swiat.konsola += komentarz
                self.swiat.konsola += "\n"
                self.swiat.plansza[self.polozenie[0] + x][self.polozenie[1] + y] = Pole()
                for i, organizm in enumerate(self.swiat.organizmy):
                    if organizm.polozenie[0] == self.polozenie[0] + x and organizm.polozenie[1] == self.polozenie[1] + y:
                        del self.swiat.organizmy[i]

    def zabijOkolice(self):
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

    def akcja(self):
        self.zabijOkolice()
        super().akcja()

    def kolizja(self, org):
        if isinstance(org, CyberOwca):
            komentarz = ""
            komentarz += str(org.nazwa)
            komentarz += " zjada "
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
            komentarz += " zjada "
            komentarz += str(self.nazwa)
            komentarz += " i umiera"
            self.swiat.konsola += komentarz
            self.swiat.konsola += "\n"
            self.swiat.plansza[self.polozenie[0]][self.polozenie[1]] = Pole()
            self.swiat.plansza[org.polozenie[0]][org.polozenie[1]] = Pole()
