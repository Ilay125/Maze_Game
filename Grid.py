from Cell import *

class Grid:
    def __init__(self, rows, cols, start):
        '''
        Initializes a grid.
        :param rows: int
        :param cols: int
        :return: None
        '''
        self.rows = rows
        self.cols = cols
        self.grid = []

        for i in range(self.cols):
            self.grid.append([])
            for j in range(self.rows):
                self.grid[i].append(Cell())

        print(self.grid)

        self.start = start
