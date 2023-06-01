from abc import abstractmethod
from World.Organism import Organism
from Plants.Field import Field
import random


class Animal(Organism):

    @abstractmethod
    def birth(self, x, y):
        pass

    def movement(self, x, y):
        if isinstance(self.world.board[self.coords[0] + x][self.coords[1] + y], Field):
            self.world.board[self.coords[0] + x][self.coords[1] + y] = self.world.board[self.coords[0]][self.coords[1]]
            self.world.board[self.coords[0]][self.coords[1]] = Field()
            self.coords[0] += x
            self.coords[1] += y
        else:
            self.world.board[self.coords[0] + x][self.coords[1] + y].collision(self)

    def __init__(self, world=None, coords=None):
        self.strength = 0
        self.age = 0
        self.initiative = 0
        self.coords = coords
        self.world = world
        self.name = "Animal"

    def reproduction(self):
        if self.coords[0] == 0:
            if self.coords[1] == 0:
                lot = random.randint(0,2)
                if lot == 0:
                    self.birth(0, 1)
                elif lot == 1:
                    self.birth(1, 1)
                elif lot == 2:
                    self.birth(1, 0)
            elif self.coords[1] == self.world.width - 1:
                lot = random.randint(0, 2)
                if lot == 0:
                    self.birth(0, -1)
                elif lot == 1:
                    self.birth(1, -1)
                elif lot == 2:
                    self.birth(1, 0)
            else:
                lot = random.randint(0, 4)
                if lot == 0:
                    self.birth(0, -1)
                elif lot == 1:
                    self.birth(1, -1)
                elif lot == 2:
                    self.birth(1, 0)
                elif lot == 3:
                    self.birth(0, 1)
                elif lot == 4:
                    self.birth(1, 1)
        elif self.coords[0] == self.world.height - 1:
            if self.coords[1] == 0:
                lot = random.randint(0,2)
                if lot == 0:
                    self.birth(0, 1)
                elif lot == 1:
                    self.birth(-1, 1)
                elif lot == 2:
                    self.birth(-1, 0)
            elif self.coords[1] == self.world.width - 1:
                lot = random.randint(0, 2)
                if lot == 0:
                    self.birth(0, -1)
                elif lot == 1:
                    self.birth(-1, -1)
                elif lot == 2:
                    self.birth(-1, 0)
            else:
                lot = random.randint(0, 4)
                if lot == 0:
                    self.birth(0, 1)
                elif lot == 1:
                    self.birth(-1, 1)
                elif lot == 2:
                    self.birth(-1, 0)
                elif lot == 3:
                    self.birth(0, -1)
                elif lot == 4:
                    self.birth(-1, -1)
        elif self.coords[1] == 0:
            lot = random.randint(0, 4)
            if lot == 0:
                self.birth(0, 1)
            elif lot == 1:
                self.birth(-1, 1)
            elif lot == 2:
                self.birth(-1, 0)
            elif lot == 3:
                self.birth(1, 1)
            elif lot == 4:
                self.birth(1, 0)
        elif self.coords[1] == self.world.width - 1:
            lot = random.randint(0, 4)
            if lot == 0:
                self.birth(0, -1)
            elif lot == 1:
                self.birth(-1, -1)
            elif lot == 2:
                self.birth(-1, 0)
            elif lot == 3:
                self.birth(1, -1)
            elif lot == 4:
                self.birth(1, 0)
        else:
            lot = random.randint(0, 7)
            if lot == 0:
                self.birth(0, 1)
            elif lot == 1:
                self.birth(1, 0)
            elif lot == 2:
                self.birth(1, 1)
            elif lot == 3:
                self.birth(-1, 0)
            elif lot == 4:
                self.birth(-1, 1)
            elif lot == 5:
                self.birth(-1, -1)
            elif lot == 6:
                self.birth(0, -1)
            elif lot == 7:
                self.birth(1, -1)

    def action(self):
        if self.coords[0] == 0:
            if self.coords[1] == 0:
                lot = random.randint(0, 2)
                if lot == 0:
                    self.movement(0, 1)
                elif lot == 1:
                    self.movement(1, 1)
                elif lot == 2:
                    self.movement(1, 0)
            elif self.coords[1] == self.world.width - 1:
                lot = random.randint(0, 2)
                if lot == 0:
                    self.movement(0, -1)
                elif lot == 1:
                    self.movement(1, -1)
                elif lot == 2:
                    self.movement(1, 0)
            else:
                lot = random.randint(0, 4)
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
        elif self.coords[0] == self.world.height - 1:
            if self.coords[1] == 0:
                lot = random.randint(0, 2)
                if lot == 0:
                    self.movement(0, 1)
                elif lot == 1:
                    self.movement(-1, 1)
                elif lot == 2:
                    self.movement(-1, 0)
            elif self.coords[1] == self.world.width - 1:
                lot = random.randint(0, 2)
                if lot == 0:
                    self.movement(0, -1)
                elif lot == 1:
                    self.movement(-1, -1)
                elif lot == 2:
                    self.movement(-1, 0)
            else:
                lot = random.randint(0, 4)
                if lot == 0:
                    self.movement(0, 1)
                elif lot == 1:
                    self.movement(-1, 1)
                elif lot == 2:
                    self.movement(-1, 0)
                elif lot == 3:
                    self.movement(0, -1)
                elif lot == 4:
                    self.movement(-1, -1)
        elif self.coords[1] == 0:
            lot = random.randint(0, 4)
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
        elif self.coords[1] == self.world.width - 1:
            lot = random.randint(0, 4)
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
        else:
            lot = random.randint(0, 7)
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

    def collision(self, org):
        if org.name == self.name:
            if org.age > 2:
                self.reproduction()
        elif org.strength >= self.strength:
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
                if organism.coords[0] == org.coords[0] and organism.coords[1] == org.coords[1]:
                    del self.world.organisms[i]
