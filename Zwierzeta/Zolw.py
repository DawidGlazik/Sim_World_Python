from Swiat.Zwierze import Zwierze
from Rosliny.Pole import Pole
import random


class Zolw(Zwierze):

    def __init__(self, swiat=None, polozenie=None, sila=2, wiek=0):
        super().__init__()
        self.swiat = swiat
        self.polozenie = polozenie
        self.inicjatywa = 1
        self.sila = sila
        self.wiek = wiek
        self.nazwa = "Zolw"

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
            self.swiat.dodajOrganizm(Zolw(self.swiat, [self.polozenie[0] + x, self.polozenie[1] + y]))

    def akcja(self):
        los = random.randint(0,3)
        if los != 0:
            return
        super().akcja()

    def kolizja(self, org):
        if isinstance(org, Zolw):
            if self.wiek > 2:
                self.rozmnazanie()
        elif org.sila < 5:
            komentarz = ""
            komentarz += str(self.nazwa)
            komentarz += str(self.polozenie)
            komentarz += " zatrzymal: "
            komentarz += str(org.nazwa)
            komentarz += str(org.polozenie)
            self.swiat.konsola += komentarz
            self.swiat.konsola += "\n"
            return
        elif org.sila > self.sila:
            komentarz = ""
            komentarz += str(org.nazwa)
            komentarz += str(org.polozenie)
            komentarz += " pokonuje: "
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
            komentarz += " przegrywa z: "
            komentarz += str(self.nazwa)
            komentarz += str(self.polozenie)
            self.swiat.konsola += komentarz
            self.swiat.konsola += "\n"
            self.swiat.plansza[org.polozenie[0]][org.polozenie[1]] = Pole()
            for i, organizm in enumerate(self.swiat.organizmy):
                if organizm.polozenie[0] == org.polozenie[0] and organizm.polozenie[1] == org.polozenie[1]:
                    del self.swiat.organizmy[i]

