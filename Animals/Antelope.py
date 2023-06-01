from World.Animal import Animal
from Plants.Field import Field
import random

class Antelope(Animal):

    def __init__(self, world=None, coords=None, strength=4, age=0):
        super().__init__()
        self.world = world
        self.coords = coords
        self.initiative = 4
        self.strength = strength
        self.age = age
        self.name = "Antelope"

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
            self.world.addOrganism(Antelope(self.world, [self.coords[0] + x, self.coords[1] + y]))

    def action(self):
        if self.coords[0] == 0:
            if self.coords[1] == 0:
                lot = random.randint(0, 4)
                if lot == 0:
                    self.movement(0, 1)
                elif lot == 1:
                    self.movement(1, 1)
                elif lot == 2:
                    self.movement(1, 0)
                elif lot == 3:
                    self.movement(0, 2)
                elif lot == 4:
                    self.movement(2, 0)
            elif self.coords[1] == self.world.width - 1:
                lot = random.randint(0, 4)
                if lot == 0:
                    self.movement(0, -1)
                elif lot == 1:
                    self.movement(1, -1)
                elif lot == 2:
                    self.movement(1, 0)
                elif lot == 3:
                    self.movement(0, -2)
                elif lot == 4:
                    self.movement(2, 0)
            else:
                lot = random.randint(0, 7)
                if lot == 0:
                    self.movement(0, -1)
                elif lot == 1:
                    self.movement(1, -1)
                elif lot == 2:
                    self.movement(1, 0)
                elif lot == 3:
                    self.movement(0, 1)
                elif lot == 4:
                    self.movement(1, 1)
                elif lot == 5 and self.coords[1] != self.world.width - 2:
                    self.movement(0, 2)
                elif lot == 6 and self.coords[0] != self.world.height - 2:
                    self.movement(2, 0)
                elif lot == 7 and  self.coords[1] != 1:
                    self.movement(0, -2)
        elif self.coords[0] == self.world.height - 1:
            if self.coords[1] == 0:
                lot = random.randint(0, 4)
                if lot == 0:
                    self.movement(0, 1)
                elif lot == 1:
                    self.movement(-1, 1)
                elif lot == 2:
                    self.movement(-1, 0)
                elif lot == 3:
                    self.movement(-2, 0)
                elif lot == 4:
                    self.movement(0, 2)
            elif self.coords[1] == self.world.width - 1:
                lot = random.randint(0, 4)
                if lot == 0:
                    self.movement(0, -1)
                elif lot == 1:
                    self.movement(-1, -1)
                elif lot == 2:
                    self.movement(-1, 0)
                elif lot == 3:
                    self.movement(-2, 0)
                elif lot == 4:
                    self.movement(0, -2)
            else:
                lot = random.randint(0, 7)
                if lot == 0:
                    self.movement(0, -1)
                elif lot == 1:
                    self.movement(-1, 1)
                elif lot == 2:
                    self.movement(-1, 0)
                elif lot == 3:
                    self.movement(0, -1)
                elif lot == 4:
                    self.movement(-1, -1)
                elif lot == 5 and self.coords[1] != self.world.width - 2:
                    self.movement(0, 2)
                elif lot == 6 and self.coords[0] != 1:
                    self.movement(-2, 0)
                elif lot == 7 and self.coords[1] != 1:
                    self.movement(0, -2)
        elif self.coords[1] == 0:
            lot = random.randint(0, 7)
            if lot == 0:
                self.movement(0, 1)
            elif lot == 1:
                self.movement(-1, 1)
            elif lot == 2:
                self.movement(-1, 0)
            elif lot == 3:
                self.movement(1, 1)
            elif lot == 4:
                self.movement(1, 0)
            elif lot == 5:
                self.movement(0, 2)
            elif lot == 6 and self.coords[0] != 1:
                self.movement(-2, 0)
            elif lot == 7 and self.coords[0] != self.world.height - 2:
                self.movement(2, 0)
        elif self.coords[1] == self.world.width - 1:
            lot = random.randint(0, 7)
            if lot == 0:
                self.movement(0, -1)
            elif lot == 1:
                self.movement(-1, -1)
            elif lot == 2:
                self.movement(-1, 0)
            elif lot == 3:
                self.movement(1, -1)
            elif lot == 4:
                self.movement(1, 0)
            elif lot == 5:
                self.movement(0, -2)
            elif lot == 6 and self.coords[0] != 1:
                self.movement(-2, 0)
            elif lot == 7 and self.coords[0] != self.world.height - 2:
                self.movement(2, 0)
        else:
            lot = random.randint(0, 11)
            if lot == 0:
                self.movement(0, 1)
            elif lot == 1:
                self.movement(1, 0)
            elif lot == 2:
                self.movement(1, 1)
            elif lot == 3:
                self.movement(-1, 0)
            elif lot == 4:
                self.movement(-1, 1)
            elif lot == 5:
                self.movement(-1, -1)
            elif lot == 6:
                self.movement(0, -1)
            elif lot == 7:
                self.movement(1, -1)
            elif lot == 8 and self.coords[0] != 1:
                self.movement(-2, 0)
            elif lot == 9 and self.coords[0] != self.world.height -2:
                self.movement(2, 0)
            elif lot == 10 and self.coords[1] != self.world.width -2:
                self.movement(0, 2)
            elif lot == 11 and self.coords[1] != 1:
                self.movement(0, -2)

    def collision(self, org):
        chance = random.randint(0,1)
        if isinstance(org, Antelope):
            if self.age > 2:
                self.reproduction()
        elif chance == 0:
            comment = ""
            comment += str(self.name)
            comment += str(self.coords)
            comment += " flees"
            self.world.console += comment
            self.world.console += "\n"
            if self.coords[1] != self.world.width - 1 and isinstance(self.world.board[self.coords[0]][self.coords[1] + 1], Field):
                self.world.board[self.coords[0]][self.coords[1] + 1] = self.world.board[self.coords[0]][self.coords[1]]
                self.world.board[self.coords[0]][self.coords[1]] = Field()
                self.coords[1] += 1
            elif self.coords[0] != self.world.height - 1 and isinstance(self.world.board[self.coords[0] + 1][self.coords[1]], Field):
                self.world.board[self.coords[0] + 1][self.coords[1]] = self.world.board[self.coords[0]][self.coords[1]]
                self.world.board[self.coords[0]][self.coords[1]] = Field()
                self.coords[0] += 1
            elif self.coords[1] != 0 and isinstance(self.world.board[self.coords[0]][self.coords[1] - 1], Field):
                self.world.board[self.coords[0]][self.coords[1] - 1] = self.world.board[self.coords[0]][self.coords[1]]
                self.world.board[self.coords[0]][self.coords[1]] = Field()
                self.coords[1] -= 1
            elif self.coords[0] != 0 and isinstance(self.world.board[self.coords[0] - 1][self.coords[1]], Field):
                self.world.board[self.coords[0] - 1][self.coords[1]] = self.world.board[self.coords[0]][self.coords[1]]
                self.world.board[self.coords[0]][self.coords[1]] = Field()
                self.coords[0] -= 1
        elif org.strength > self.strength:
            comment = ""
            comment += str(org.name)
            comment += str(org.coords)
            comment += " defeats "
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
            comment += " beaten by "
            comment += str(self.name)
            comment += str(self.coords)
            self.world.console += comment
            self.world.console += "\n"
            self.world.board[org.coords[0]][org.coords[1]] = Field()
            for i, organism in enumerate(self.world.organisms):
                if organism.coords[0] == self.coords[0] and organism.coords[1] == self.coords[1]:
                    del self.world.organisms[i]
