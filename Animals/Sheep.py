from World.Animal import Animal
from Plants.Field import Field


class Sheep(Animal):

    def __init__(self, world=None, coords=None, strength=4, age=0):
        super().__init__()
        self.world = world
        self.coords = coords
        self.initiative = 4
        self.strength = strength
        self.age = age
        self.name = "Sheep"

    def birth(self, x, y):
        if isinstance(self.world.board[self.coords[0] + x][self.coords[1] + y], Field):
            comment = ""
            comment += "New birth: "
            comment += str(self.name)
            comment += "("
            comment += str(self.coords[0] + x + 1)
            comment += ","
            comment += str(self.coords[1] + y + 1)
            comment += ")"
            self.world.console += comment
            self.world.console += "\n"
            self.world.addOrganism(Sheep(self.world, [self.coords[0] + x, self.coords[1] + y]))
