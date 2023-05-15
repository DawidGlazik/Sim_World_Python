from Swiat.Zwierze import Zwierze
from Rosliny.Pole import Pole


class CyberOwca(Zwierze):

    def __init__(self, swiat=None, polozenie=None, sila=11, wiek=0):
        super().__init__()
        self.swiat = swiat
        self.polozenie = polozenie
        self.inicjatywa = 4
        self.sila = sila
        self.wiek = wiek
        self.nazwa = "CyberOwca"

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
            self.swiat.dodajOrganizm(CyberOwca(self.swiat, (self.polozenie[0] + x, self.polozenie[1] + y)))
