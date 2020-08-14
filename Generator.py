from Grid import Grid as g
import random

class Generator:
    def __init__(self, rows, cols):
        self.start = (random.randrange(0, cols), random.randrange(0, rows))
        self.Grid = g(rows, cols)
        self.loc = self.start
        self.way = []
        self.rows = rows
        self.cols = cols
        self.impossible = [self.start]
        self.done = False
        self.last = ()

    def deadend(self):

        self.impossible.append(self.loc)

        backc = self.loc[1] - self.way[-2][1]
        backr = self.loc[0] - self.way[-2][0]

        self.way.pop()
        self.way.pop()

        if backc > 0:
            return "up"
        if backc < 0:
            return "down"
        if backr > 0:
            return "left"
        if backr < 0:
            return "right"

    def turn(self, loc):
        c, r = self.loc
        poss = []
        found = False

        if len(self.way)+len(self.impossible)-1 == self.rows*self.cols:
            self.last = self.loc
            self.done = True
            return

        if r > 0:
            if not loc.up and (c, r-1) not in self.way and (c, r-1) not in self.impossible:
                poss.append("up")
                found = True
        if r + 1 < self.rows:
            if not loc.down and (c, r+1) not in self.way and (c, r+1) not in self.impossible:
                poss.append("down")
                found = True
        if c > 0:
            if not loc.left and (c-1, r) not in self.way and (c-1, r) not in self.impossible:
                poss.append("left")
                found = True
        if c + 1 < self.cols:
            if not loc.right and (c+1, r) not in self.way and (c+1, r) not in self.impossible:
                poss.append("right")
                found = True
                
        if not found:
            return self.deadend()
        return random.choice(poss)

    def move(self):
        c, r = self.loc
        cell = self.Grid.grid[c][r]

        self.way.append(self.loc)

        turn = self.turn(cell)
        if turn == "up":
            cell.up = True
            self.loc = (c, r - 1)
            self.Grid.grid[self.loc[0]][self.loc[1]].down = True

        elif turn == "down":
            cell.down = True
            self.loc = (c, r + 1)
            self.Grid.grid[self.loc[0]][self.loc[1]].up = True

        elif turn == "left":
            cell.left = True
            self.loc = (c-1, r)
            self.Grid.grid[self.loc[0]][self.loc[1]].right = True

        elif turn == "right":
            cell.right = True
            self.loc = (c + 1, r)
            self.Grid.grid[self.loc[0]][self.loc[1]].left = True

