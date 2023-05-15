from Swiat.Roslina import Roslina
from Rosliny.Pole import Pole


class WilczeJagody(Roslina):

    def __init__(self, swiat=None, polozenie=None, wiek=0):
        super().__init__()
        self.swiat = swiat
        self.polozenie = polozenie
        self.sila = 99
        self.wiek = wiek
        self.nazwa = "WilczeJagody"

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
            self.swiat.dodajOrganizm(WilczeJagody(self.swiat, (self.polozenie[0] + x, self.polozenie[1] + y)))

    def kolizja(self, org):
        komentarz = ""
        komentarz += str(org.nazwa)
        komentarz += str(org.polozenie)
        komentarz += " zjada "
        komentarz += str(self.nazwa)
        komentarz += str(self.polozenie)
        komentarz += "i umiera"
        self.swiat.konsola += komentarz
        self.swiat.konsola += "\n"
        self.swiat.plansza[self.polozenie[0]][self.polozenie[1]] = Pole()
        self.swiat.plansza[org.polozenie[0]][org.polozenie[1]] = Pole()
        for i, organizm in enumerate(self.swiat.organizmy):
            if organizm.polozenie[0] == self.polozenie[0] and organizm.polozenie[1] == self.polozenie[1]:
                del self.swiat.organizmy[i]
            if organizm.polozenie[0] == org.polozenie[0] and organizm.polozenie[1] == org.polozenie[1]:
                del self.swiat.organizmy[i]
