#read in the file for discrete source(body force), 2d for now

import numpy as np

class TableReader():

    def __init__(self, table):
        [self.coord, self.fb] = np.hsplit(np.loadtxt(table), 2)

        self.coord = self.coord.reshape(-1, 3)
        self.fb = self.fb.reshape(-1, 3)
