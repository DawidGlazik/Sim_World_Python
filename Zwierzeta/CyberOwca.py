from Swiat.Zwierze import Zwierze
from Rosliny.Pole import Pole
from Rosliny import BarszczSosnowskiego
import queue


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
            self.swiat.dodajOrganizm(CyberOwca(self.swiat, [self.polozenie[0] + x, self.polozenie[1] + y]))

    def akcja(self):
        kolejka = queue.Queue()
        i = self.polozenie[0]
        k = self.polozenie[1]
        kolejka.put((i, k))
        czyZnalazl = False
        visited = [[0 for _ in range(self.swiat.szerokosc)] for _ in range(self.swiat.wysokosc)]
        while not kolejka.empty():
            element = kolejka.get()
            i = element[0]
            k = element[1]
            if isinstance(self.swiat.plansza[i][k], BarszczSosnowskiego.BarszczSosnowskiego):
                czyZnalazl = True
                break
            else:
                if i > 0 and not visited[i - 1][k]:
                    kolejka.put((i - 1, k))
                    visited[i - 1][k] = 1
                if i < self.swiat.wysokosc - 1 and not visited[i + 1][k]:
                    kolejka.put((i + 1, k))
                    visited[i + 1][k] = 1
                if k > 0 and not visited[i][k - 1]:
                    kolejka.put((i, k - 1))
                    visited[i][k - 1] = 1
                if k < self.swiat.szerokosc - 1 and not visited[i][k + 1]:
                    kolejka.put((i, k + 1))
                    visited[i][k + 1] = 1

        if czyZnalazl:
            if i - self.polozenie[0] > 0:
                kierunek1 = 1
            elif i - self.polozenie[0] < 0:
                kierunek1 = -1
            else:
                kierunek1 = 0

            if k - self.polozenie[1] > 0:
                kierunek2 = 1
            elif k - self.polozenie[1] < 0:
                kierunek2 = -1
            else:
                kierunek2 = 0

            self.ruch(kierunek1, kierunek2)
        else:
            super().akcja()