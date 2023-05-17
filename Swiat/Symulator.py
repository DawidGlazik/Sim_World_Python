import random
from Swiat.Okno import Okno
from Rosliny.Pole import Pole
from Swiat.Czlowiek import Czlowiek
from Rosliny.BarszczSosnowskiego import BarszczSosnowskiego
from Rosliny.Mlecz import Mlecz
from Rosliny.Trawa import Trawa
from Rosliny.Guarana import Guarana
from Rosliny.WilczeJagody import WilczeJagody
from Zwierzeta.Zolw import Zolw
from Zwierzeta.Lis import Lis
from Zwierzeta.Owca import Owca
from Zwierzeta.Wilk import Wilk
from Zwierzeta.Antylopa import Antylopa
from Zwierzeta.CyberOwca import CyberOwca
import os
from tkinter import simpledialog


class Symulator:

    def __init__(self, szerokosc=None, wysokosc=None):
        self.tura = 0
        self.konsola = ""
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.organizmy = []
        self.plansza = [[Pole() for _ in range(szerokosc)] for _ in range(wysokosc)]
        liczbaOrganizmow = szerokosc * wysokosc / 15
        self.dodajOrganizm(Czlowiek(self, [int(wysokosc / 2), int(szerokosc / 2)]))
        for i in range(0, int(liczbaOrganizmow)):
            random1 = random.randint(0, wysokosc - 1)
            random2 = random.randint(0, szerokosc - 1)
            random3 = random.randint(0, 1000)
            if isinstance(self.plansza[random1][random2], Pole):
                if i < 11:
                    k = i
                else:
                    k = random3 % 11
                if k == 0:
                    self.dodajOrganizm(BarszczSosnowskiego(self, [random1, random2]))
                elif k == 1:
                    self.dodajOrganizm(Guarana(self, [random1, random2]))
                elif k == 2:
                    self.dodajOrganizm(Mlecz(self, [random1, random2]))
                elif k == 3:
                    self.dodajOrganizm(Trawa(self, [random1, random2]))
                elif k == 4:
                    self.dodajOrganizm(WilczeJagody(self, [random1, random2]))
                elif k == 5:
                    self.dodajOrganizm(Antylopa(self, [random1, random2]))
                elif k == 6:
                    self.dodajOrganizm(Lis(self, [random1, random2]))
                elif k == 7:
                    self.dodajOrganizm(Owca(self, [random1, random2]))
                elif k == 8:
                    self.dodajOrganizm(Wilk(self, [random1, random2]))
                elif k == 9:
                    self.dodajOrganizm(Zolw(self, [random1, random2]))
                elif k == 10:
                    self.dodajOrganizm(CyberOwca(self, [random1, random2]))

    def rysujSwiat(self, plansza):
        okno = Okno(self, plansza)
        okno.rysuj()

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
        for organizm in self.organizmy:
            organizm.wiek += 1
        self.tura += 1

    def zapisz(self):
        nazwa_pliku = simpledialog.askstring(None, "Wprowadź nazwę pliku:")
        if nazwa_pliku:
            print("Wybrana nazwa pliku:", nazwa_pliku)
            with open(nazwa_pliku, 'w') as plik:
                dane = str(self.tura) + " " + str(self.szerokosc) + " " + str(self.wysokosc) + "\n"
                plik.write(dane)
                for organizm in self.organizmy:
                    dane = str(organizm.nazwa) + " " + str(organizm.polozenie[0]) + " " + str(organizm.polozenie[1]) + " " + str(organizm.sila) + " " + str(organizm.wiek) + " "
                    if isinstance(organizm, Czlowiek):
                        dane += str(organizm.trwanie) + " " + str(organizm.przerwa)
                    dane += "\n"
                    plik.write(dane)
                self.konsola += "Pomyslnie zapisano stan symulacji"
                return
        return

    def wczytaj(self):
        nazwa_pliku = simpledialog.askstring(None, "Wprowadź nazwę pliku:")
        if nazwa_pliku:
            if os.path.isfile(nazwa_pliku):
                del self.plansza
                self.organizmy = []
                with open(nazwa_pliku, 'r') as plik:
                    linia = plik.readline().rstrip().split(" ")
                    self.tura = int(linia[0])
                    self.szerokosc = int(linia[1])
                    self.wysokosc = int(linia[2])
                    self.plansza = [[Pole() for _ in range(self.szerokosc)] for _ in range(self.wysokosc)]
                    for _linia in plik:
                        linia = _linia.rstrip().split(" ")
                        nazwa = linia[0]
                        x = int(linia[1])
                        y = int(linia[2])
                        sila = int(linia[3])
                        wiek = int(linia[4])
                        if nazwa == "BarszczSosnowskiego":
                            self.dodajOrganizm(BarszczSosnowskiego(self, [x, y], wiek))
                        elif nazwa == "Guarana":
                            self.dodajOrganizm(Guarana(self, [x, y], wiek))
                        elif nazwa == "Mlecz":
                            self.dodajOrganizm(Mlecz(self, [x, y], wiek))
                        elif nazwa == "Trawa":
                            self.dodajOrganizm(Trawa(self, [x, y], wiek))
                        elif nazwa == "WilczeJagody":
                            self.dodajOrganizm(WilczeJagody(self, [x, y], wiek))
                        elif nazwa == "Antylopa":
                            self.dodajOrganizm(Antylopa(self, [x, y], sila, wiek))
                        elif nazwa == "Lis":
                            self.dodajOrganizm(Lis(self, [x, y], sila, wiek))
                        elif nazwa == "Owca":
                            self.dodajOrganizm(Owca(self, [x, y], sila, wiek))
                        elif nazwa == "Wilk":
                            self.dodajOrganizm(Wilk(self, [x, y], sila, wiek))
                        elif nazwa == "Zolw":
                            self.dodajOrganizm(Zolw(self, [x, y], sila, wiek))
                        elif nazwa == "CyberOwca":
                            self.dodajOrganizm(CyberOwca(self, [x, y], sila, wiek))
                        elif nazwa == "Czlowiek":
                            trwanie = int(linia[5])
                            przerwa = int(linia[6])
                            self.dodajOrganizm(Czlowiek(self, [x, y], sila, wiek, trwanie, przerwa))
                self.konsola += "Pomyslnie wczytano stan symulacji"
            else:
                self.konsola += "Plik nie istnieje"


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

