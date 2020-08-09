from Cell import *

class Grid:
    def __init__(self, rows, cols):
        '''
        Initializes a grid.
        :param rows: int
        :param cols: int
        :return: None
        '''
        self.grid = []

        for i in range(cols):
            self.grid.append([])
            for j in range(rows):
                self.grid[i].append(Cell())

        print(self.grid)

