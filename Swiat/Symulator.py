import random

from Rosliny.Pole import Pole
from Swiat.Czlowiek import Czlowiek
from Rosliny.BarszczSosnowskiego import BarszczSosnowskiego

class Symulator:

    def __init__(self, szerokosc=None, wysokosc=None):
        self.tura = 0
        self.konsola = ""
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.organizmy = [Pole()]
        self.plansza = [[Pole() for _ in range(szerokosc)] for _ in range(wysokosc)]
        numberOfOrganisms = szerokosc * wysokosc / 15
        self.dodajOrganizm(Czlowiek(self, (wysokosc / 2, szerokosc / 2)))
        for i in range(0, int(numberOfOrganisms)):
            random1 = random.randint(0, wysokosc - 1)
            random2 = random.randint(0, szerokosc - 1)
            random3 = random.randint(0, 1000)
            if isinstance(self.plansza[random1][random2], Pole):
                if i < 10:
                    k = i
                else:
                    k = random.randint(0,9)
                if k == 0:
                    self.dodajOrganizm(BarszczSosnowskiego(self, (random1, random2)))

    def rysujSwiat(self):
        self.wypiszOrganizmy()

    def dodajOrganizm(self, nowy):
        self.plansza[int(nowy.polozenie[0])][int(nowy.polozenie[1])] = nowy
        if len(self.organizmy) == 0:
            self.organizmy.append(nowy)
        else:
            for i in range(len(self.organizmy)):
                if nowy.inicjatywa > self.organizmy[i].inicjatywa:
                    self.organizmy.insert(i, nowy)
                    return
            self.organizmy.append(nowy)

    def wykonajTure(self, kierunek):
        for organizm in self.organizmy:
            if isinstance(organizm, Czlowiek):
                tmp = organizm
                tmp.akcja(kierunek)
                if 5 > tmp.trwanie > 0:
                    tmp.calopalenie()
                elif tmp.przerwa > 0:
                    tmp.przerwa -= 1
                else:
                    tmp.trwanie = 5
            elif isinstance(organizm, BarszczSosnowskiego):
                tmp = organizm
                tmp.akcja()
            else:
                organizm.akcja()

    def zapisz(self):
        pass

    def wczytaj(self):
        pass

    def wypiszOrganizmy(self):
        for organizm in self.organizmy:
            print(organizm.nazwa)

    def rozpocznijCalopalenie(self):
        for organizm in self.organizmy:
            if isinstance(organizm, Czlowiek):
                tmp = organizm
                if tmp.trwanie == 5:
                    komentarz = "Czlowiek rozpoczyna calopalenie."
                    self.konsola += komentarz
                    self.konsola += "\n"
                    tmp.calopalenie()
                    if tmp.przerwa != 5:
                        tmp.przerwa += 5

