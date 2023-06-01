from World.Animal import Animal
from Plants.Field import Field
import random


class Turtle(Animal):

    def __init__(self, world=None, coords=None, strength=2, age=0):
        super().__init__()
        self.world = world
        self.coords = coords
        self.initiative = 1
        self.strength = strength
        self.age = age
        self.name = "Turtle"

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
            self.world.addOrganism(Turtle(self.world, [self.coords[0] + x, self.coords[1] + y]))

    def action(self):
        lot = random.randint(0,3)
        if lot != 0:
            return
        super().action()

    def collision(self, org):
        if isinstance(org, Turtle):
            if self.age > 2:
                self.reproduction()
        elif org.strength < 5:
            comment = ""
            comment += str(self.name)
            comment += str(self.coords)
            comment += " stops: "
            comment += str(org.name)
            comment += str(org.coords)
            self.world.console += comment
            self.world.console += "\n"
            return
        elif org.strength > self.strength:
            comment = ""
            comment += str(org.name)
            comment += str(org.coords)
            comment += " defeats: "
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
            comment += str(org.coords)
            comment += " beaten by: "
            comment += str(self.name)
            comment += str(self.coords)
            self.world.console += comment
            self.world.console += "\n"
            self.world.board[org.coords[0]][org.coords[1]] = Field()
            for i, organism in enumerate(self.world.organisms):
                if organism.coords[0] == org.coords[0] and organism.coords[1] == org.coords[1]:
                    del self.world.organisms[i]

