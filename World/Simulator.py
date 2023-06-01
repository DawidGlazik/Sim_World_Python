import random
from World.Window import Window
from Plants.Field import Field
from World.Human import Human
from Plants.Hogweed import Hogweed
from Plants.Milt import Milt
from Plants.Grass import Grass
from Plants.Guarana import Guarana
from Plants.DeadlyNightshades import DeadlyNightshade
from Animals.Turtle import Turtle
from Animals.Fox import Fox
from Animals.Sheep import Sheep
from Animals.Wolf import Wolf
from Animals.Antelope import Antelope
from Animals.CyberSheep import CyberSheep
import os
from tkinter import simpledialog


class Simulator:

    def __init__(self, width=None, height=None):
        self.turn = 0
        self.console = ""
        self.width = width
        self.height = height
        self.organisms = []
        self.board = [[Field() for _ in range(width)] for _ in range(height)]
        numberOfOrganisms = width * height / 15
        self.addOrganism(Human(self, [int(height / 2), int(width / 2)]))
        for i in range(0, int(numberOfOrganisms)):
            random1 = random.randint(0, height - 1)
            random2 = random.randint(0, width - 1)
            random3 = random.randint(0, 1000)
            if isinstance(self.board[random1][random2], Field):
                if i < 11:
                    k = i
                else:
                    k = random3 % 11
                if k == 0:
                    self.addOrganism(Hogweed(self, [random1, random2]))
                elif k == 1:
                    self.addOrganism(Guarana(self, [random1, random2]))
                elif k == 2:
                    self.addOrganism(Milt(self, [random1, random2]))
                elif k == 3:
                    self.addOrganism(Grass(self, [random1, random2]))
                elif k == 4:
                    self.addOrganism(DeadlyNightshade(self, [random1, random2]))
                elif k == 5:
                    self.addOrganism(Antelope(self, [random1, random2]))
                elif k == 6:
                    self.addOrganism(Fox(self, [random1, random2]))
                elif k == 7:
                    self.addOrganism(Sheep(self, [random1, random2]))
                elif k == 8:
                    self.addOrganism(Wolf(self, [random1, random2]))
                elif k == 9:
                    self.addOrganism(Turtle(self, [random1, random2]))
                elif k == 10:
                    self.addOrganism(CyberSheep(self, [random1, random2]))

    def printWorld(self, board):
        window = Window(self, board)
        window.print()

    def addOrganism(self, new):
        self.board[int(new.coords[0])][int(new.coords[1])] = new
        if len(self.organisms) == 0:
            self.organisms.append(new)
        else:
            for i in range(len(self.organisms)):
                if new.initiative > self.organisms[i].initiative:
                    self.organisms.insert(i, new)
                    return
            self.organisms.append(new)

    def handleTurn(self, direction):
        for organism in self.organisms:
            if isinstance(organism, Human):
                tmp = organism
                tmp.action(direction)
                if 5 > tmp.lasting > 0:
                    tmp.calopalenie()
                elif tmp.brake_ > 0:
                    tmp.brake_ -= 1
                else:
                    tmp.lasting = 5
            elif isinstance(organism, Hogweed):
                tmp = organism
                tmp.action()
            else:
                organism.action()
        for organism in self.organisms:
            organism.age += 1
        self.turn += 1

    def save(self):
        file_name = simpledialog.askstring(None, "Insert file name:")
        if file_name:
            print("File name:", file_name)
            with open(file_name, 'w') as file:
                data = str(self.turn) + " " + str(self.width) + " " + str(self.height) + "\n"
                file.write(data)
                for organism in self.organisms:
                    data = str(organism.name) + " " + str(organism.coords[0]) + " " + str(organism.coords[1]) + " " + str(organism.strength) + " " + str(organism.age) + " "
                    if isinstance(organism, Human):
                        data += str(organism.lasting) + " " + str(organism.brake_)
                    data += "\n"
                    file.write(data)
                self.console += "Saved"
                return
        return

    def load(self):
        file_name = simpledialog.askstring(None, "Insert file name:")
        if file_name:
            if os.path.isfile(file_name):
                del self.board
                self.organisms = []
                with open(file_name, 'r') as file:
                    line = file.readline().rstrip().split(" ")
                    self.turn = int(line[0])
                    self.width = int(line[1])
                    self.height = int(line[2])
                    self.board = [[Field() for _ in range(self.width)] for _ in range(self.height)]
                    for _line in file:
                        line = _line.rstrip().split(" ")
                        name = line[0]
                        x = int(line[1])
                        y = int(line[2])
                        strength = int(line[3])
                        age = int(line[4])
                        if name == "Hogweed":
                            self.addOrganism(Hogweed(self, [x, y], age))
                        elif name == "Guarana":
                            self.addOrganism(Guarana(self, [x, y], age))
                        elif name == "Milt":
                            self.addOrganism(Milt(self, [x, y], age))
                        elif name == "Grass":
                            self.addOrganism(Grass(self, [x, y], age))
                        elif name == "Deadly_Nightshade":
                            self.addOrganism(DeadlyNightshade(self, [x, y], age))
                        elif name == "Antelope":
                            self.addOrganism(Antelope(self, [x, y], strength, age))
                        elif name == "Fox":
                            self.addOrganism(Fox(self, [x, y], strength, age))
                        elif name == "Sheep":
                            self.addOrganism(Sheep(self, [x, y], strength, age))
                        elif name == "Wolf":
                            self.addOrganism(Wolf(self, [x, y], strength, age))
                        elif name == "Turtle":
                            self.addOrganism(Turtle(self, [x, y], strength, age))
                        elif name == "CyberSheep":
                            self.addOrganism(CyberSheep(self, [x, y], strength, age))
                        elif name == "Human":
                            lasting = int(line[5])
                            brake_ = int(line[6])
                            self.addOrganism(Human(self, [x, y], strength, age, lasting, brake_))
                self.console += "Loaded"
            else:
                self.console += "File doesn't exist"


    def printOrganisms(self):
        for organism in self.organisms:
            print(organism.name)

    def startCalopalenie(self):
        for organism in self.organisms:
            if isinstance(organism, Human):
                tmp = organism
                if tmp.lasting == 5:
                    comment = "Human starts calopalenie."
                    self.console += comment
                    self.console += "\n"
                    tmp.calopalenie()
                    if tmp.brake_ != 5:
                        tmp.brake_ += 5

