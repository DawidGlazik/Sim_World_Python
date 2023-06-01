from abc import abstractmethod
from Plants import Field
from World.Organism import Organism
import random


class Plant(Organism):

    @abstractmethod
    def checkAndSeed(self, x, y):
        pass

    def __init__(self, world=None, coords=None):
        self.strength = 0
        self.age = 0
        self.initiative = 0
        self.coords = coords
        self.world = world
        self.name = "Plant"

    def action(self):
        lot1 = random.randint(0, 14)
        if lot1 != 0:
            return
        if self.coords[0] == 0:
            lot2 = random.randint(0, 10)
            if self.coords[1] == 0:
                if lot2 == 0:
                    self.checkAndSeed(0, 1)
                elif lot2 == 1:
                    self.checkAndSeed(1, 1)
                elif lot2 == 2:
                    self.checkAndSeed(1, 0)
            elif self.coords[1] == self.world.width - 1:
                if lot2 == 3:
                    self.checkAndSeed(0, -1)
                elif lot2 == 4:
                    self.checkAndSeed(1, -1)
                elif lot2 == 5:
                    self.checkAndSeed(1, 0)
            else:
                if lot2 == 6:
                    self.checkAndSeed(0, -1)
                elif lot2 == 7:
                    self.checkAndSeed(1, -1)
                elif lot2 == 8:
                    self.checkAndSeed(1, 0)
                elif lot2 == 9:
                    self.checkAndSeed(0, 1)
                elif lot2 == 10:
                    self.checkAndSeed(1, 1)
        elif self.coords[0] == self.world.height - 1:
            lot2 = random.randint(0, 10)
            if self.coords[1] == 0:
                if lot2 == 0:
                    self.checkAndSeed(0, 1)
                elif lot2 == 1:
                    self.checkAndSeed(-1, 1)
                elif lot2 == 2:
                    self.checkAndSeed(-1, 0)
            elif self.coords[1] == self.world.width - 1:
                if lot2 == 3:
                    self.checkAndSeed(0, -1)
                elif lot2 == 4:
                    self.checkAndSeed(-1, -1)
                elif lot2 == 5:
                    self.checkAndSeed(-1, 0)
            else:
                if lot2 == 6:
                    self.checkAndSeed(0, 1)
                elif lot2 == 7:
                    self.checkAndSeed(-1, 1)
                elif lot2 == 8:
                    self.checkAndSeed(-1, 0)
                elif lot2 == 9:
                    self.checkAndSeed(0, -1)
                elif lot2 == 10:
                    self.checkAndSeed(-1, -1)
        elif self.coords[0] == self.world.height - 1:
            lot2 = random.randint(0, 10)
            if self.coords[1] == 0:
                if lot2 == 0:
                    self.checkAndSeed(0, 1)
                elif lot2 == 1:
                    self.checkAndSeed(-1, 1)
                elif lot2 == 2:
                    self.checkAndSeed(-1, 0)
            elif self.coords[1] == self.world.width - 1:
                if lot2 == 3:
                    self.checkAndSeed(0, -1)
                elif lot2 == 4:
                    self.checkAndSeed(-1, -1)
                elif lot2 == 5:
                    self.checkAndSeed(-1, 0)
            else:
                if lot2 == 6:
                    self.checkAndSeed(0, 1)
                elif lot2 == 7:
                    self.checkAndSeed(-1, 1)
                elif lot2 == 8:
                    self.checkAndSeed(-1, 0)
                elif lot2 == 9:
                    self.checkAndSeed(0, -1)
                elif lot2 == 10:
                    self.checkAndSeed(-1, -1)
        elif self.coords[1] == 0:
            lot2 = random.randint(0, 4)
            if lot2 == 0:
                self.checkAndSeed(0, 1)
            elif lot2 == 1:
                self.checkAndSeed(-1, 1)
            elif lot2 == 2:
                self.checkAndSeed(-1, 0)
            elif lot2 == 3:
                self.checkAndSeed(1, 1)
            elif lot2 == 4:
                self.checkAndSeed(1, 0)
        elif self.coords[1] == self.world.width - 1:
            lot2 = random.randint(0, 4)
            if lot2 == 0:
                self.checkAndSeed(0, -1)
            elif lot2 == 1:
                self.checkAndSeed(-1, -1)
            elif lot2 == 2:
                self.checkAndSeed(-1, 0)
            elif lot2 == 3:
                self.checkAndSeed(1, -1)
            elif lot2 == 4:
                self.checkAndSeed(1, 0)
        else:
            lot2 = random.randint(0, 7)
            if lot2 == 0:
                self.checkAndSeed(0, 1)
            elif lot2 == 1:
                self.checkAndSeed(1, 0)
            elif lot2 == 2:
                self.checkAndSeed(1, 1)
            elif lot2 == 3:
                self.checkAndSeed(-1, 0)
            elif lot2 == 4:
                self.checkAndSeed(-1, 1)
            elif lot2 == 5:
                self.checkAndSeed(-1, -1)
            elif lot2 == 6:
                self.checkAndSeed(0, -1)
            elif lot2 == 7:
                self.checkAndSeed(1, -1)

    def collision(self, org):
        comment = ""
        comment += str(org.name)
        comment += str(org.coords)
        comment += " eats "
        comment += str(self.name)
        comment += str(self.coords)
        self.world.console += comment
        self.world.console += "\n"
        for i, organism in enumerate(self.world.organisms):
            if organism.coords[0] == self.coords[0] and organism.coords[1] == self.coords[1]:
                del self.world.organisms[i]
        self.world.board[self.coords[0]][self.coords[1]] = org
        self.world.board[org.coords[0]][org.coords[1]] = Field.Field()
        org.coords[0] = self.coords[0]
        org.coords[1] = self.coords[1]
