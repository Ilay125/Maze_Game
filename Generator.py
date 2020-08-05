from Grid import Grid as g
import random

class Generator:
    def __init__(self, rows, cols):
        self.start = (random.randrange(0, rows), random.randrange(0, cols))
        self.Grid = g(rows, cols, self.start)
        self.loc = self.start
        self.way = [self.start]
        self.found = False


    def deadend(self):
        r, c = self.loc
        cell = self.Grid.grid[r, c]

        cell.possible = False
        self.way.remove(self.loc)

        self.loc = self.way[-1]

        return False


    def turn(self, loc):
        poss = []

        while not self.found:
            if not loc.up:
                poss.append("up")
                self.found = True
            if not loc.down:
                poss.append("down")
                self.found = True
            if not loc.left:
                poss.append("left")
                self.found = True
            if not loc.right:
                poss.append("right")
                self.found = True

            if len(poss) == 0:
                self.found = self.deadend()

        return random.choice(poss)


    def move(self):
        r, c = self.loc
        cell = self.Grid.grid[r, c]

        cell.been = True
        self.way.append(self.loc)

        turn = self.turn(cell)
        if turn == "up":
            cell.up = True
            self.Grid.grid[r, c - 1].down = True

            self.loc = (r, c - 1)

        elif turn == "down":
            cell.down = True
            self.Grid.grid[r, c + 1].up = True

            self.loc = (r, c + 1)

        elif turn == "left":
            cell.left = True
            self.Grid.grid[r - 1, c].right = True

            self.loc = (r - 1, c)

        elif turn == "right":
            cell.right = True
            self.Grid.grid[r + 1, c].left = True

            self.loc = (r + 1, c)


