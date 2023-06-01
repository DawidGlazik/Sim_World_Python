from World.Animal import Animal
from Plants.Field import Field


class Human(Animal):

    def __init__(self, world=None, coords=None, strength=5, age=0, lasting=5, _break=0):
        super().__init__(world, coords)
        self.strength = strength
        self.initiative = 4
        self.age = age
        self.world = world
        self.coords = coords
        self.lasting = lasting
        self.brake_ = _break
        self.name = "Human"

    def checkAndKill(self, x, y):
        if not isinstance(self.world.board[self.coords[0] + x][self.coords[1] + y], Field):
            comment = ""
            comment += str(self.world.board[self.coords[0] + x][self.coords[1] + y].name)
            comment += str(self.world.board[self.coords[0] + x][self.coords[1] + y].coords)
            comment += " killed by (calopalenie) "
            comment += str(self.name)
            comment += str(self.coords)
            self.world.console += comment
            self.world.console += "\n"
            self.world.board[self.coords[0] + x][self.coords[1] + y] = Field()
            for i, organism in enumerate(self.world.organisms):
                if organism.coords[0] == self.coords[0] + x and organism.coords[1] == self.coords[1] + y:
                    del self.world.organisms[i]

    def action(self, direction):
        if direction == 0:
            return
        elif direction == 1:
            if self.coords[0] == 0:
                return
            else:
                if isinstance(self.world.board[self.coords[0] - 1][self.coords[1]], Field):
                    self.world.board[self.coords[0] - 1][self.coords[1]] = \
                        self.world.board[self.coords[0]][self.coords[1]]
                    self.world.board[self.coords[0]][self.coords[1]] = Field()
                    self.coords[0] -= 1
                else:
                    self.world.board[self.coords[0] - 1][self.coords[1]].collision(self)
        elif direction == 2:
            if self.coords[0] == self.world.height - 1:
                return
            else:
                if isinstance(self.world.board[self.coords[0] + 1][self.coords[1]], Field):
                    self.world.board[self.coords[0] + 1][self.coords[1]] = \
                        self.world.board[self.coords[0]][self.coords[1]]
                    self.world.board[self.coords[0]][self.coords[1]] = Field()
                    self.coords[0] += 1
                else:
                    self.world.board[self.coords[0] + 1][self.coords[1]].collision(self)
        elif direction == 3:
            if self.coords[1] == 0:
                return
            else:
                if isinstance(self.world.board[self.coords[0]][self.coords[1] - 1], Field):
                    self.world.board[self.coords[0]][self.coords[1] - 1] = \
                        self.world.board[self.coords[0]][self.coords[1]]
                    self.world.board[self.coords[0]][self.coords[1]] = Field()
                    self.coords[1] -= 1
                else:
                    self.world.board[self.coords[0]][self.coords[1] - 1].collision(self)
        elif direction == 4:
            if self.coords[1] == self.world.width - 1:
                return
            else:
                if isinstance(self.world.board[self.coords[0]][self.coords[1] + 1], Field):
                    self.world.board[self.coords[0]][self.coords[1] + 1] = \
                        self.world.board[self.coords[0]][self.coords[1]]
                    self.world.board[self.coords[0]][self.coords[1]] = Field()
                    self.coords[1] += 1
                else:
                    self.world.board[self.coords[0]][self.coords[1] + 1].collision(self)

    def calopalenie(self):
        self.lasting -= 1
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

    def birth(self, x, y):
        print("")