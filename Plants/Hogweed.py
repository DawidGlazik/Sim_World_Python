from World.Plant import Plant
from Plants.Field import Field
from World.Animal import Animal
from Animals.CyberSheep import CyberSheep

class Hogweed(Plant):

    def __init__(self, world=None, coords=None, age=0):
        super().__init__()
        self.world = world
        self.coords = coords
        self.strength = 10
        self.age = age
        self.name = "Hogweed"

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
            self.world.addOrganism(Hogweed(self.world, (self.coords[0] + x, self.coords[1] + y)))

    def checkAndKill(self, x, y):
        if isinstance(self.world.board[self.coords[0] + x][self.coords[1] + y], Animal):
            if isinstance(self.world.board[self.coords[0] + x][self.coords[1] + y], CyberSheep):
                return
            else:
                comment = ""
                comment += str(self.world.board[self.coords[0] + x][self.coords[1] + y].name)
                comment += str(self.world.board[self.coords[0] + x][self.coords[1] + y].coords)
                comment += " killed by "
                comment += str(self.name)
                comment += str(self.coords)
                self.world.console += comment
                self.world.console += "\n"
                self.world.board[self.coords[0] + x][self.coords[1] + y] = Field()
                for i, organism in enumerate(self.world.organisms):
                    if organism.coords[0] == self.coords[0] + x and organism.coords[1] == self.coords[1] + y:
                        del self.world.organisms[i]

    def killArea(self):
        if self.coords[0] == 0:
            if self.coords[1] == 0:
                self.checkAndKill(0, 1)
                self.checkAndKill(1, 1)
                self.checkAndKill(1, 0)
            elif self.coords[1] == self.world.width - 1:
                self.checkAndKill(0, -1)
                self.checkAndKill(1, -1)
                self.checkAndKill(1, 0)
            else:
                self.checkAndKill(0, -1)
                self.checkAndKill(1, -1)
                self.checkAndKill(1, 0)
                self.checkAndKill(0, 1)
                self.checkAndKill(1, 1)
        elif self.coords[0] == self.world.height - 1:
            if self.coords[1] == 0:
                self.checkAndKill(0, 1)
                self.checkAndKill(-1, 1)
                self.checkAndKill(-1, 0)
            elif self.coords[1] == self.world.width - 1:
                self.checkAndKill(0, -1)
                self.checkAndKill(-1, -1)
                self.checkAndKill(-1, 0)
            else:
                self.checkAndKill(0, 1)
                self.checkAndKill(-1, 1)
                self.checkAndKill(-1, 0)
                self.checkAndKill(0, -1)
                self.checkAndKill(-1, -1)
        elif self.coords[1] == 0:
            self.checkAndKill(0, 1)
            self.checkAndKill(-1, 1)
            self.checkAndKill(-1, 0)
            self.checkAndKill(1, 1)
            self.checkAndKill(1, 0)
        elif self.coords[1] == self.world.width - 1:
            self.checkAndKill(0, -1)
            self.checkAndKill(-1, -1)
            self.checkAndKill(-1, 0)
            self.checkAndKill(1, -1)
            self.checkAndKill(1, 0)
        else:
            self.checkAndKill(0, 1)
            self.checkAndKill(1, 0)
            self.checkAndKill(1, 1)
            self.checkAndKill(-1, 0)
            self.checkAndKill(-1, 1)
            self.checkAndKill(-1, -1)
            self.checkAndKill(0, -1)
            self.checkAndKill(1, -1)

    def action(self):
        self.killArea()
        super().action()

    def collision(self, org):
        if isinstance(org, CyberSheep):
            comment = ""
            comment += str(org.name)
            comment += " eats "
            comment += str(self.name)
            comment += str(self.coords)
            self.world.console += comment
            self.world.console += "\n"
            for i, organism in enumerate(self.world.organisms):
                if organism.coords[0] == self.coords[0] and organism.coords[1] == self.coords[1]:
                    del self.world.organisms[i]
            self.world.board[self.coords[0]][self.coords[1]] = org
            self.world.board[org.coords[0]][org.coords[1]] = Field()
            org.coords[0] = self.coords[0]
            org.coords[1] = self.coords[1]
        else:
            comment = ""
            comment += str(org.name)
            comment += " eats "
            comment += str(self.name)
            comment += " and dies"
            self.world.console += comment
            self.world.console += "\n"
            self.world.board[self.coords[0]][self.coords[1]] = Field()
            self.world.board[org.coords[0]][org.coords[1]] = Field()
