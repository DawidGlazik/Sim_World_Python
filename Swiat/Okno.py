import  tkinter as tk
from tkinter import scrolledtext
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
from Zwierzeta.CyberOwca import CyberOwca


class Okno:

    def __init__(self, swiat, plansza):
        self.root = tk.Tk()
        self.root.title("Dawid Glazik s193069")
        self.canvas = None
        self.dialog = None
        self.swiat = swiat
        self.plansza = plansza
        self.text_area = None

    def rysuj(self):
        self.canvas = tk.Canvas(self.root, width=len(self.plansza[0]) * 30, height=len(self.plansza) * 30, cursor="hand2")
        self.canvas.pack()

        for row in range(len(self.plansza)):
            for col in range(len(self.plansza[row])):
                x1 = col * 30
                y1 = row * 30
                x2 = x1 + 30
                y2 = y1 + 30

                if isinstance(self.plansza[row][col], Pole):
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                elif isinstance(self.plansza[row][col], Czlowiek):
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="gray")
                elif isinstance(self.plansza[row][col], Zwierze):
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="yellow")
                    if isinstance(self.plansza[row][col], Wilk):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="W")
                    elif isinstance(self.plansza[row][col], Owca):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="O")
                    elif isinstance(self.plansza[row][col], Lis):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="L")
                    elif isinstance(self.plansza[row][col], Zolw):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="Z")
                    elif isinstance(self.plansza[row][col], Antylopa):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="A")
                    elif isinstance(self.plansza[row][col], CyberOwca):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="C")
                elif isinstance(self.plansza[row][col], Roslina):
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")
                    if isinstance(self.plansza[row][col], Trawa):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="t")
                    elif isinstance(self.plansza[row][col], Mlecz):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="m")
                    elif isinstance(self.plansza[row][col], Guarana):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="g")
                    elif isinstance(self.plansza[row][col], WilczeJagody):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="w")
                    elif isinstance(self.plansza[row][col], BarszczSosnowskiego):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="b")
                self.canvas.bind("<Button-1>", self.klikniecie)

        przyciski = tk.Frame(self.root)
        przyciski.pack()

        przycisk1 = tk.Button(przyciski, text="Tura", command=self.tura)
        przycisk2 = tk.Button(przyciski, text="Zapisz", command=self.zapisz)
        przycisk3 = tk.Button(przyciski, text="Wczytaj", command=self.wczytaj)
        przycisk4 = tk.Button(przyciski, text="Calopalenie", command=self.calopalenie)

        przycisk1.pack(side="left")
        przycisk2.pack(side="left")
        przycisk3.pack(side="left")
        przycisk4.pack(side="left")

        self.text_area = scrolledtext.ScrolledText(self.root, height=10)
        self.text_area.insert(tk.END, "Tura: "+str(self.swiat.tura)+"\n")
        self.text_area.configure(state="disabled")
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.root.bind('<Up>', self.gora)
        self.root.bind('<Down>', self.dol)
        self.root.bind('<Left>', self.lewo)
        self.root.bind('<Right>', self.prawo)

        self.root.mainloop()

    def odswiez(self):
        self.canvas.delete("all")  # Usunięcie wszystkich elementów z płótna

        for row in range(len(self.plansza)):
            for col in range(len(self.plansza[row])):
                x1 = col * 30
                y1 = row * 30
                x2 = x1 + 30
                y2 = y1 + 30

                if isinstance(self.plansza[row][col], Pole):
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                elif isinstance(self.plansza[row][col], Czlowiek):
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="gray")
                elif isinstance(self.plansza[row][col], Zwierze):
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="yellow")
                    if isinstance(self.plansza[row][col], Wilk):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="W")
                    elif isinstance(self.plansza[row][col], Owca):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="O")
                    elif isinstance(self.plansza[row][col], Lis):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="L")
                    elif isinstance(self.plansza[row][col], Zolw):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="Z")
                    elif isinstance(self.plansza[row][col], Antylopa):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="A")
                    elif isinstance(self.plansza[row][col], CyberOwca):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="C")
                elif isinstance(self.plansza[row][col], Roslina):
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")
                    if isinstance(self.plansza[row][col], Trawa):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="t")
                    elif isinstance(self.plansza[row][col], Mlecz):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="m")
                    elif isinstance(self.plansza[row][col], Guarana):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="g")
                    elif isinstance(self.plansza[row][col], WilczeJagody):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="w")
                    elif isinstance(self.plansza[row][col], BarszczSosnowskiego):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="b")
                self.canvas.bind("<Button-1>", self.klikniecie)

        self.text_area.configure(state="normal")
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "Tura: "+str(self.swiat.tura)+"\n")
        self.text_area.insert(tk.END, self.swiat.konsola)
        self.text_area.configure(state="disabled")

        self.swiat.konsola = ""

    def tura(self):
        self.swiat.wykonajTure(0)
        self.odswiez()

    def zapisz(self):
        self.swiat.zapisz()
        self.text_area.configure(state="normal")
        self.text_area.insert(tk.END, self.swiat.konsola)
        self.text_area.configure(state="disabled")
        self.odswiez()


    def wczytaj(self):
        self.swiat.wczytaj()
        self.plansza = self.swiat.plansza
        self.text_area.configure(state="normal")
        self.text_area.insert(tk.END, self.swiat.konsola)
        self.text_area.configure(state="disabled")
        self.odswiez()

    def calopalenie(self):
        self.swiat.rozpocznijCalopalenie()
        self.text_area.configure(state="normal")
        self.text_area.insert(tk.END, self.swiat.konsola)
        self.text_area.configure(state="disabled")
        self.odswiez()

    def gora(self, event):
        for organizm in self.swiat.organizmy:
            if isinstance(organizm, Czlowiek):
                self.swiat.wykonajTure(1)
                self.odswiez()
                break

    def dol(self, event):
        for organizm in self.swiat.organizmy:
            if isinstance(organizm, Czlowiek):
                self.swiat.wykonajTure(2)
                self.odswiez()
                break

    def lewo(self, event):
        for organizm in self.swiat.organizmy:
            if isinstance(organizm, Czlowiek):
                self.swiat.wykonajTure(3)
                self.odswiez()
                break

    def prawo(self, event):
        for organizm in self.swiat.organizmy:
            if isinstance(organizm, Czlowiek):
                self.swiat.wykonajTure(4)
                self.odswiez()
                break

    def klikniecie(self, event):
        x = event.x // 30
        y = event.y // 30
        if y >= self.swiat.wysokosc or x >= self.swiat.szerokosc:
            return
        if not isinstance(self.swiat.plansza[y][x], Pole):
            self.swiat.konsola += "Miejsce zajete"
            self.text_area.configure(state="normal")
            self.text_area.insert(tk.END, self.swiat.konsola)
            self.text_area.configure(state="disabled")
            self.odswiez()
            return
        else:
            self.dialog = tk.Toplevel(self.root)
            self.dialog.title("Wybierz opcję")
            opcje = ["Wilk", "Owca", "Lis", "Zolw", "Antylopa", "CyberOwca", "Trawa", "Mlecz", "Guarana", "Wilcze Jagody",
                     "Barszcz Sosnowskiego"]
            for opcja in opcje:
                button = tk.Button(self.dialog, text=opcja)
                button.configure(command=lambda wybrano=opcja: self.handle_button_click(wybrano, y ,x))
                button.pack(expand=True, fill=tk.BOTH)

    def handle_button_click(self, wybrano, x, y):
        self.dialog.destroy()
        if wybrano == "Barszcz Sosnowskiego":
            self.swiat.dodajOrganizm(BarszczSosnowskiego(self.swiat, [x, y]))
        elif wybrano == "Guarana":
            self.swiat.dodajOrganizm(Guarana(self.swiat, [x, y]))
        elif wybrano == "Mlecz":
            self.swiat.dodajOrganizm(Mlecz(self.swiat, [x, y]))
        elif wybrano == "Trawa":
            self.swiat.dodajOrganizm(Trawa(self.swiat, [x, y]))
        elif wybrano == "Wilcze Jagody":
            self.swiat.dodajOrganizm(WilczeJagody(self.swiat, [x, y]))
        elif wybrano == "Antylopa":
            self.swiat.dodajOrganizm(Antylopa(self.swiat, [x, y]))
        elif wybrano == "Lis":
            self.swiat.dodajOrganizm(Lis(self.swiat, [x, y]))
        elif wybrano == "Owca":
            self.swiat.dodajOrganizm(Owca(self.swiat, [x, y]))
        elif wybrano == "Wilk":
            self.swiat.dodajOrganizm(Wilk(self.swiat, [x, y]))
        elif wybrano == "Zolw":
            self.swiat.dodajOrganizm(Zolw(self.swiat, [x, y]))
        elif wybrano == "CyberOwca":
            self.swiat.dodajOrganizm(CyberOwca(self.swiat, [x, y]))
        self.odswiez()

