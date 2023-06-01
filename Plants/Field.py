from World.Plant import Plant


class Field(Plant):
    def __init__(self, world=None, coords=None):
        super().__init__()
        self.name = "Pole"
        self.strength = 0
        self.age = 0
        self.world = world
        self.coords = coords

    def checkAndSeed(self, x, y):
        pass
