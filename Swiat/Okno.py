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
        self.swiat = swiat
        self.plansza = plansza
        self.text_area = None

    def rysuj(self):
        self.canvas = tk.Canvas(self.root, width=len(self.plansza[0]) * 30, height=len(self.plansza) * 30)
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

        button_frame = tk.Frame(self.root)
        button_frame.pack()

        button1 = tk.Button(button_frame, text="Tura", command=self.tura)
        button2 = tk.Button(button_frame, text="Zapisz", command=self.zapisz)
        button3 = tk.Button(button_frame, text="Wczytaj", command=self.wczytaj)
        button4 = tk.Button(button_frame, text="Calopalenie", command=self.calopalenie)

        button1.pack(side="left")
        button2.pack(side="left")
        button3.pack(side="left")
        button4.pack(side="left")

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
        # Implementacja logiki dla przycisku Zapisz
        print("Zapisano świat")

    def wczytaj(self):
        print("Wczytano świat")

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