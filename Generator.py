from Grid import Grid as g
import random

class Generator:
    def __init__(self, rows, cols):
        self.start = (random.randrange(0, rows), random.randrange(0, cols))
        self.Grid = g(rows, cols, self.start)
        self.loc = self.start
        self.way = [self.start]
        self.rows = rows
        self.cols = cols

        self.Grid.grid[self.start[0]][self.start[1]].possible = False

    def deadend(self):
        r, c = self.loc
        cell = self.Grid.grid[r][c]

        cell.possible = False
        self.way.remove(self.loc)

        self.loc = self.way[-1]

    def turn(self, loc):
        r, c = self.loc
        poss = []
        found = False

        while not found:

            if c-1 > -1:
                if not loc.up and not self.Grid.grid[r][c - 1].been and self.Grid.grid[r][c - 1].possible:
                    poss.append("up")
                    found = True
            if c+1 < self.cols:
                if not loc.down and not self.Grid.grid[r][c + 1].been and self.Grid.grid[r][c + 1].possible:
                    poss.append("down")
                    found = True
            if r-1 > -1:
                if not loc.left and not self.Grid.grid[r - 1][c].been and self.Grid.grid[r - 1][c].possible:
                    poss.append("left")
                    found = True
            if r+1 < self.rows:
                if not loc.right and not self.Grid.grid[r + 1][c].been and self.Grid.grid[r + 1][c].possible:
                    poss.append("right")
                    found = True

            if not found:
                self.deadend()
                return self.turn(self.Grid.grid[self.loc[0]][self.loc[1]])


        return random.choice(poss)

    def move(self):
        print(self.way)

        r, c = self.loc
        cell = self.Grid.grid[r][c]

        cell.been = True
        self.way.append(self.loc)

        turn = self.turn(cell)
        if turn == "up":
            cell.up = True
            self.Grid.grid[r][c - 1].down = True

            self.loc = (r, c - 1)

        elif turn == "down":
            cell.down = True
            self.Grid.grid[r][c + 1].up = True

            self.loc = (r, c + 1)

        elif turn == "left":
            cell.left = True
            self.Grid.grid[r - 1][c].right = True

            self.loc = (r - 1, c)

        elif turn == "right":
            cell.right = True
            self.Grid.grid[r + 1][c].left = True

            self.loc = (r + 1, c)


