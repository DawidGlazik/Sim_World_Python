from World.Plant import Plant
from Plants.Field import Field


class Guarana(Plant):

    def __init__(self, world=None, coords=None, age=0):
        super().__init__()
        self.world = world
        self.coords = coords
        self.strength = 0
        self.age = age
        self.name = "Guarana"

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
            self.world.addOrganism(Guarana(self.world, (self.coords[0] + x, self.coords[1] + y)))

    def collision(self, org):
        comment = ""
        comment += str(org.name)
        comment += str(org.coords)
        comment += " - strength + 3 "
        comment += str(self.name)
        comment += str(self.coords)
        self.world.console += comment
        self.world.console += "\n"
        org.strength += 3
        for i, organism in enumerate(self.world.organisms):
            if organism.coords[0] == self.coords[0] and organism.coords[1] == self.coords[1]:
                del self.world.organisms[i]
        self.world.board[self.coords[0]][self.coords[1]] = org
        self.world.board[org.coords[0]][org.coords[1]] = Field()
        org.coords[0] = self.coords[0]
        org.coords[1] = self.coords[1]
