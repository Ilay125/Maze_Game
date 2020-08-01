class Cell:
    def __init__(self):
        '''
        Initializes a cell.
        :returns: None
        '''
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.been = False
        self.possible = False
