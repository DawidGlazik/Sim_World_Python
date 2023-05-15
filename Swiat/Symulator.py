import random
import tkinter as tk
from Swiat.Zwierze import Zwierze
from Swiat.Roslina import Roslina
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

class Symulator:

    def __init__(self, szerokosc=None, wysokosc=None):
        self.tura = 0
        self.konsola = ""
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.organizmy = []
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
                    k = random3 % 10
                if k == 0:
                    self.dodajOrganizm(BarszczSosnowskiego(self, (random1, random2)))
                elif k == 1:
                    self.dodajOrganizm(Guarana(self, (random1, random2)))
                elif k == 2:
                    self.dodajOrganizm(Mlecz(self, (random1, random2)))
                elif k == 3:
                    self.dodajOrganizm(Trawa(self, (random1, random2)))
                elif k == 4:
                    self.dodajOrganizm(WilczeJagody(self, (random1, random2)))
                elif k == 5:
                    self.dodajOrganizm(Antylopa(self, (random1, random2)))
                elif k == 6:
                    self.dodajOrganizm(Lis(self, (random1, random2)))
                elif k == 7:
                    self.dodajOrganizm(Owca(self, (random1, random2)))
                elif k == 8:
                    self.dodajOrganizm(Wilk(self, (random1, random2)))
                elif k == 9:
                    self.dodajOrganizm(Zolw(self, (random1, random2)))

    def rysujSwiat(self, plansza):
        root = tk.Tk()

        canvas = tk.Canvas(root, width=len(plansza[0]) * 30, height=len(plansza) * 30)
        canvas.pack()

        for row in range(len(plansza)):
            for col in range(len(plansza[row])):
                x1 = col * 30
                y1 = row * 30
                x2 = x1 + 30
                y2 = y1 + 30

                if isinstance(plansza[row][col], Pole):
                    canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                elif isinstance(plansza[row][col], Czlowiek):
                    canvas.create_rectangle(x1, y1, x2, y2, fill="gray")
                elif isinstance(plansza[row][col], Zwierze):
                    canvas.create_rectangle(x1, y1, x2, y2, fill="yellow")
                elif isinstance(plansza[row][col], Roslina):
                    canvas.create_rectangle(x1, y1, x2, y2, fill="green")

        # Tworzenie kontenera na przyciski
        button_frame = tk.Frame(root)
        button_frame.pack()

        # Tworzenie przycisków
        button1 = tk.Button(button_frame, text="Tura")
        button2 = tk.Button(button_frame, text="Zapisz")
        button3 = tk.Button(button_frame, text="Wczytaj")
        button4 = tk.Button(button_frame, text="Calopalenie")

        # Umieszczenie przycisków w kontenerze
        button1.pack(side="left")
        button2.pack(side="left")
        button3.pack(side="left")
        button4.pack(side="left")

        # Tworzenie miejsca na tekst
        text_label = tk.Label(root, text="Tekst")
        text_label.pack(side="left")
        root.mainloop()
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

