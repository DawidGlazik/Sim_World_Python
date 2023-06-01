import  tkinter as tk
from tkinter import scrolledtext
from World.Animal import Animal
from World.Plant import Plant
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


class Window:

    def __init__(self, world, board):
        self.root = tk.Tk()
        self.root.title("Dawid Glazik")
        self.canvas = None
        self.dialog = None
        self.world = world
        self.board = board
        self.text_area = None

    def print(self):
        self.canvas = tk.Canvas(self.root, width=len(self.board[0]) * 30, height=len(self.board) * 30, cursor="hand2")
        self.canvas.pack()

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                x1 = col * 30
                y1 = row * 30
                x2 = x1 + 30
                y2 = y1 + 30

                if isinstance(self.board[row][col], Field):
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                elif isinstance(self.board[row][col], Human):
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="gray")
                elif isinstance(self.board[row][col], Animal):
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="yellow")
                    if isinstance(self.board[row][col], Wolf):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="W")
                    elif isinstance(self.board[row][col], Sheep):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="S")
                    elif isinstance(self.board[row][col], Fox):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="F")
                    elif isinstance(self.board[row][col], Turtle):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="T")
                    elif isinstance(self.board[row][col], Antelope):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="A")
                    elif isinstance(self.board[row][col], CyberSheep):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="C")
                elif isinstance(self.board[row][col], Plant):
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")
                    if isinstance(self.board[row][col], Grass):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="gr")
                    elif isinstance(self.board[row][col], Milt):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="m")
                    elif isinstance(self.board[row][col], Guarana):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="g")
                    elif isinstance(self.board[row][col], DeadlyNightshade):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="d")
                    elif isinstance(self.board[row][col], Hogweed):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="h")
                self.canvas.bind("<Button-1>", self.click)

        buttons = tk.Frame(self.root)
        buttons.pack()

        button1 = tk.Button(buttons, text="Turn", command=self.turn)
        button2 = tk.Button(buttons, text="Save", command=self.save)
        button3 = tk.Button(buttons, text="Load", command=self.load)
        button4 = tk.Button(buttons, text="Calopalenie", command=self.calopalenie)

        button1.pack(side="left")
        button2.pack(side="left")
        button3.pack(side="left")
        button4.pack(side="left")

        self.text_area = scrolledtext.ScrolledText(self.root, height=10)
        self.text_area.insert(tk.END, "Turn: " + str(self.world.turn) + "\n")
        self.text_area.configure(state="disabled")
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.root.bind('<Up>', self.up)
        self.root.bind('<Down>', self.down)
        self.root.bind('<Left>', self.left)
        self.root.bind('<Right>', self.right)

        self.root.mainloop()

    def refresh(self):
        self.canvas.delete("all")

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                x1 = col * 30
                y1 = row * 30
                x2 = x1 + 30
                y2 = y1 + 30

                if isinstance(self.board[row][col], Field):
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                elif isinstance(self.board[row][col], Human):
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="gray")
                elif isinstance(self.board[row][col], Animal):
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="yellow")
                    if isinstance(self.board[row][col], Wolf):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="W")
                    elif isinstance(self.board[row][col], Sheep):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="S")
                    elif isinstance(self.board[row][col], Fox):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="F")
                    elif isinstance(self.board[row][col], Turtle):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="T")
                    elif isinstance(self.board[row][col], Antelope):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="A")
                    elif isinstance(self.board[row][col], CyberSheep):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="C")
                elif isinstance(self.board[row][col], Plant):
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")
                    if isinstance(self.board[row][col], Grass):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="gr")
                    elif isinstance(self.board[row][col], Milt):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="m")
                    elif isinstance(self.board[row][col], Guarana):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="g")
                    elif isinstance(self.board[row][col], DeadlyNightshade):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="d")
                    elif isinstance(self.board[row][col], Hogweed):
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="h")
                self.canvas.bind("<Button-1>", self.click)

        self.text_area.configure(state="normal")
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "Turn: " + str(self.world.turn) + "\n")
        self.text_area.insert(tk.END, self.world.console)
        self.text_area.configure(state="disabled")

        self.world.console = ""

    def turn(self):
        self.world.handleTurn(0)
        self.refresh()

    def save(self):
        self.world.save()
        self.text_area.configure(state="normal")
        self.text_area.insert(tk.END, self.world.console)
        self.text_area.configure(state="disabled")
        self.refresh()


    def load(self):
        self.world.load()
        self.board = self.world.board
        self.text_area.configure(state="normal")
        self.text_area.insert(tk.END, self.world.console)
        self.text_area.configure(state="disabled")
        self.refresh()

    def calopalenie(self):
        self.world.startCalopalenie()
        self.text_area.configure(state="normal")
        self.text_area.insert(tk.END, self.world.console)
        self.text_area.configure(state="disabled")
        self.refresh()

    def up(self, event):
        for organism in self.world.organisms:
            if isinstance(organism, Human):
                self.world.handleTurn(1)
                self.refresh()
                break

    def down(self, event):
        for organism in self.world.organisms:
            if isinstance(organism, Human):
                self.world.handleTurn(2)
                self.refresh()
                break

    def left(self, event):
        for organism in self.world.organisms:
            if isinstance(organism, Human):
                self.world.handleTurn(3)
                self.refresh()
                break

    def right(self, event):
        for organism in self.world.organisms:
            if isinstance(organism, Human):
                self.world.handleTurn(4)
                self.refresh()
                break

    def click(self, event):
        x = event.x // 30
        y = event.y // 30
        if y >= self.world.height or x >= self.world.width:
            return
        if not isinstance(self.world.board[y][x], Field):
            self.world.console += "Field occupied"
            self.text_area.configure(state="normal")
            self.text_area.insert(tk.END, self.world.console)
            self.text_area.configure(state="disabled")
            self.refresh()
            return
        else:
            self.dialog = tk.Toplevel(self.root)
            self.dialog.title("Choose one")
            options = ["Wolf", "Sheep", "Fox", "Turtle", "Antelope", "CyberSheep", "Grass", "Milt", "Guarana", "Deadly Nightshade",
                     "Hogweed"]
            for option in options:
                button = tk.Button(self.dialog, text=option)
                button.configure(command=lambda chosen=option: self.handle_button_click(chosen, y, x))
                button.pack(expand=True, fill=tk.BOTH)

    def handle_button_click(self, chosen, x, y):
        self.dialog.destroy()
        if chosen == "Hogweed":
            self.world.addOrganism(Hogweed(self.world, [x, y]))
        elif chosen == "Guarana":
            self.world.addOrganism(Guarana(self.world, [x, y]))
        elif chosen == "Milt":
            self.world.addOrganism(Milt(self.world, [x, y]))
        elif chosen == "Grass":
            self.world.addOrganism(Grass(self.world, [x, y]))
        elif chosen == "Deadly Nightshade":
            self.world.addOrganism(DeadlyNightshade(self.world, [x, y]))
        elif chosen == "Antelope":
            self.world.addOrganism(Antelope(self.world, [x, y]))
        elif chosen == "Fox":
            self.world.addOrganism(Fox(self.world, [x, y]))
        elif chosen == "Sheep":
            self.world.addOrganism(Sheep(self.world, [x, y]))
        elif chosen == "Wolf":
            self.world.addOrganism(Wilk(self.world, [x, y]))
        elif chosen == "Turtle":
            self.world.addOrganism(Turtle(self.world, [x, y]))
        elif chosen == "CyberSheep":
            self.world.addOrganism(CyberSheep(self.world, [x, y]))
        self.refresh()

