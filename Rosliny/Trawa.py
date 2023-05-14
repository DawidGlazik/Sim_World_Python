from Swiat.Roslina import Roslina
from Rosliny.Pole import Pole


class Trawa(Roslina):

    def __init__(self, swiat=None, polozenie=None, wiek=0):
        super().__init__()
        self.swiat = swiat
        self.polozenie = polozenie
        self.sila = 0
        self.wiek = wiek
        self.nazwa = "Trawa"

    def sprawdzIZasiej(self, x, y):
        if isinstance(self.swiat.plansza[self.polozenie[0] + x][self.polozenie[1] + y], Pole):
            komentarz = ""
            komentarz += "Zasiano "
            komentarz += self.nazwa
            komentarz += "("
            komentarz += self.polozenie[0] + x + 1
            komentarz += ","
            komentarz += self.polozenie[1] + y + 1
            komentarz += ")"
            self.swiat.konsola += komentarz
            self.swiat.dodajOrganizm(Trawa(self.swiat, (self.polozenie[0] + x, self.polozenie[1] + y)))
