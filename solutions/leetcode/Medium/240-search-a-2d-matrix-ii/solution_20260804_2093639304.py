class Solution:
    def searchMatrix(self, mat, x):
        m, n = len(mat), len(mat[0])
        row, col = 0, n - 1
        while row < m and col >= 0:
            if mat[row][col] == x:
                return True
            elif mat[row][col] < x:
                row += 1
            else:
                col -= 1
        return False
