class NumMatrix(object):

    def __init__(self, matrix):
        self.matrix = matrix        

    def update(self, row, col, val):
        self.matrix[row][col] = val

    def sumRegion(self, row1, col1, row2, col2):
        sm = 0
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                sm += self.matrix[i][j]

        return sm
