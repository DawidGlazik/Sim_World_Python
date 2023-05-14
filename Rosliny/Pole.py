from Swiat.Roslina import Roslina


class Pole(Roslina):
    def __init__(self, swiat=None, polozenie=None):
        super().__init__()
        self.nazwa = "Pole"
        self.sila = 0
        self.wiek = 0
        self.swiat = swiat
        self.polozenie = polozenie

    def sprawdzIZasiej(self, x, y):
        pass
