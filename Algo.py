from Grid import *
import random

class Algorithm:
    def __init__(self, rows, cols):
        self.start = (random.randrange(0, rows), random.randrange(0, cols))
        self.grid = Grid(rows, cols, self.start)
        self.cell = self.start
        self.way = [self.start]


    def turn(self):
        pass

    def move(self):
        pass


