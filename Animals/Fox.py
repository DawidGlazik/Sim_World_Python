from World.Animal import Animal
from Plants.Field import Field


class Fox(Animal):

    def __init__(self, world=None, coords=None, strength=3, age=0):
        super().__init__()
        self.world = world
        self.coords = coords
        self.initiative = 7
        self.strength = strength
        self.age = age
        self.name = "Fox"

    def movement(self, x, y):
        if isinstance(self.world.board[self.coords[0] + x][self.coords[1] + y], Field):
            self.world.board[self.coords[0] + x][self.coords[1] + y] = self.world.board[self.coords[0]][self.coords[1]]
            self.world.board[self.coords[0]][self.coords[1]] = Field()
            self.coords[0] += x
            self.coords[1] += y
        else:
            if self.world.board[self.coords[0] + x][self.coords[1] + y].strength > self.strength:
                return
            else:
                self.world.board[self.coords[0] + x][self.coords[1] + y].collision(self)

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
            self.world.addOrganism(Fox(self.world, [self.coords[0] + x, self.coords[1] + y]))
