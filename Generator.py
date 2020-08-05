from Grid import Grid as g
import random

class Generator:
    def __init__(self, rows, cols):
        self.start = (random.randrange(0, rows), random.randrange(0, cols))
        self.Grid = g(rows, cols, self.start)
        self.loc = self.start
        self.way = []
        self.rows = rows
        self.cols = cols

        self.Grid.grid[self.start[0]][self.start[1]].possible = False

    def deadend(self):
        c, r = self.loc
        cell = self.Grid.grid[c][r]

        cell.possible = False
        self.way.remove(self.loc)

        self.loc = self.way[-1]

    def turn(self, loc):
        c, r = self.loc
        poss = []
        found = False

        while not found:

            if c > 0:
                if not loc.up and not self.Grid.grid[c-1][r].been and self.Grid.grid[c - 1][r].possible:
                    poss.append("up")
                    found = True
            if c + 1 < self.cols:
                if not loc.down and not self.Grid.grid[c+1][r].been and self.Grid.grid[c + 1][r].possible:
                    poss.append("down")
                    found = True
            if r > 0:
                if not loc.left and not self.Grid.grid[c][r-1].been and self.Grid.grid[c][r - 1].possible:
                    poss.append("left")
                    found = True
            if r + 1 < self.rows:
                if not loc.right and not self.Grid.grid[c][r+1].been and self.Grid.grid[c][r + 1].possible:
                    poss.append("right")
                    found = True

            if not found:
                self.deadend()
                return self.turn(self.Grid.grid[self.loc[0]][self.loc[1]])


        return random.choice(poss)

    def move(self):
        c, r = self.loc
        cell = self.Grid.grid[c][r]

        cell.been = True

        print(self.loc)

        self.way.append(self.loc)

        turn = self.turn(cell)
        if turn == "up":
            cell.up = True
            self.Grid.grid[c - 1][r].down = True

            self.loc = (c - 1, r)

        elif turn == "down":
            cell.down = True
            self.Grid.grid[c + 1][r].up = True

            self.loc = (c + 1, r)

        elif turn == "left":
            cell.left = True
            self.Grid.grid[c][r-1].right = True

            self.loc = (c, r-1)

        elif turn == "right":
            cell.right = True
            self.Grid.grid[c][r + 1].left = True

            self.loc = (c, r + 1)


