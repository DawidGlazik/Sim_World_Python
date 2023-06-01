from World.Animal import Animal
from Plants.Field import Field
from Plants import Hogweed
import queue


class CyberSheep(Animal):

    def __init__(self, world=None, coords=None, strength=11, age=0):
        super().__init__()
        self.world = world
        self.coords = coords
        self.initiative = 4
        self.strength = strength
        self.age = age
        self.name = "CyberSheep"

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
            self.world.addOrganism(CyberSheep(self.world, [self.coords[0] + x, self.coords[1] + y]))

    def action(self):
        que = queue.Queue()
        i = self.coords[0]
        k = self.coords[1]
        que.put((i, k))
        found = False
        visited = [[0 for _ in range(self.world.width)] for _ in range(self.world.height)]
        while not que.empty():
            element = que.get()
            i = element[0]
            k = element[1]
            if isinstance(self.world.board[i][k], Hogweed.Hogweed):
                found = True
                break
            else:
                if i > 0 and not visited[i - 1][k]:
                    que.put((i - 1, k))
                    visited[i - 1][k] = 1
                if i < self.world.height - 1 and not visited[i + 1][k]:
                    que.put((i + 1, k))
                    visited[i + 1][k] = 1
                if k > 0 and not visited[i][k - 1]:
                    que.put((i, k - 1))
                    visited[i][k - 1] = 1
                if k < self.world.width - 1 and not visited[i][k + 1]:
                    que.put((i, k + 1))
                    visited[i][k + 1] = 1

        if found:
            if i - self.coords[0] > 0:
                direction1 = 1
            elif i - self.coords[0] < 0:
                direction1 = -1
            else:
                direction1 = 0

            if k - self.coords[1] > 0:
                direction2 = 1
            elif k - self.coords[1] < 0:
                direction2 = -1
            else:
                direction2 = 0

            self.movement(direction1, direction2)
        else:
            super().action()