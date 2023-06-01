from World.Plant import Plant
from Plants.Field import Field


class Milt(Plant):

    def __init__(self, world=None, coords=None, age=0):
        super().__init__()
        self.world = world
        self.coords = coords
        self.strength = 0
        self.age = age
        self.name = "Milt"

    def checkAndSeed(self, x, y):
        if isinstance(self.world.board[self.coords[0] + x][self.coords[1] + y], Field):
            comment = ""
            comment += "Seed "
            comment += str(self.name)
            comment += "("
            comment += str(self.coords[0] + x + 1)
            comment += ","
            comment += str(self.coords[1] + y + 1)
            comment += ")"
            self.world.console += comment
            self.world.console += "\n"
            self.world.addOrganism(Milt(self.world, (self.coords[0] + x, self.coords[1] + y)))

    def action(self):
        for i in range(3):
            super().action()