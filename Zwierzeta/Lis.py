from Swiat.Zwierze import Zwierze
from Rosliny.Pole import Pole


class Lis(Zwierze):

    def __init__(self, swiat=None, polozenie=None, sila=3, wiek=0):
        super().__init__()
        self.swiat = swiat
        self.polozenie = polozenie
        self.inicjatywa = 7
        self.sila = sila
        self.wiek = wiek
        self.nazwa = "Lis"

    def ruch(self, x, y):
        if isinstance(self.swiat.plansza[self.polozenie[0] + x][self.polozenie[1] + y], Pole):
            self.swiat.plansza[self.polozenie[0] + x][self.polozenie[1] + y] = self.swiat.plansza[self.polozenie[0]][self.polozenie[1]];
            self.swiat.plansza[self.polozenie[0]][self.polozenie[1]] = Pole()
            self.polozenie[0] += x
            self.polozenie[1] += y
        else:
            if self.swiat.plansza[self.polozenie[0] + x][self.polozenie[1] + y].sila > self.sila:
                return
            else:
                self.swiat.plansza[self.polozenie[0] + x][self.polozenie[1] + y].kolizja(self)

    def narodziny(self, x, y):
        if isinstance(self.swiat.plansza[self.polozenie[0] + x][self.polozenie[1] + y], Pole):
            komentarz = ""
            komentarz += "Narodziny organizmu: "
            komentarz += str(self.nazwa)
            komentarz += "("
            komentarz += str(self.polozenie[0] + x + 1)
            komentarz += ","
            komentarz += str(self.polozenie[1] + y + 1)
            komentarz += ")"
            self.swiat.konsola += komentarz
            self.swiat.konsola += "\n"
            self.swiat.dodajOrganizm(Lis(self.swiat, (self.polozenie[0] + x, self.polozenie[1] + y)))
