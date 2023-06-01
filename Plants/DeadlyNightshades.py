from World.Plant import Plant
from Plants.Field import Field


class DeadlyNightshade(Plant):

    def __init__(self, world=None, coords=None, age=0):
        super().__init__()
        self.world = world
        self.coords = coords
        self.strength = 99
        self.age = age
        self.name = "Deadly_Nightshade"

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
            self.world.addOrganism(DeadlyNightshade(self.world, (self.coords[0] + x, self.coords[1] + y)))

    def collision(self, org):
        comment = ""
        comment += str(org.name)
        comment += str(org.coords)
        comment += " eats "
        comment += str(self.name)
        comment += str(self.coords)
        comment += " and dies"
        self.world.console += comment
        self.world.console += "\n"
        self.world.board[self.coords[0]][self.coords[1]] = Field()
        self.world.board[org.coords[0]][org.coords[1]] = Field()
        for i, organism in enumerate(self.world.organisms):
            if organism.coords[0] == self.coords[0] and organism.coords[1] == self.coords[1]:
                del self.world.organisms[i]
            if organism.coords[0] == org.coords[0] and organism.coords[1] == org.coords[1]:
                del self.world.organisms[i]
