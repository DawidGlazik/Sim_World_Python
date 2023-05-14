from Swiat.Zwierze import Zwierze
from Rosliny.Pole import Pole


class Wilk(Zwierze):

    def __init__(self, swiat=None, polozenie=None, sila=9, wiek=0):
        super().__init__()
        self.swiat = swiat
        self.polozenie = polozenie
        self.inicjatywa = 5
        self.sila = sila
        self.wiek = wiek
        self.nazwa = "Wilk"

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
            self.swiat.dodajOrganizm(Wilk(self.swiat, (self.polozenie[0] + x, self.polozenie[1] + y)))

