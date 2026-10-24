class Solution:
    def searchMatrix(self, mat, x):
        m, n = len(mat), len(mat[0])
        low, high = 0, m * n - 1
        while low <= high:
            mid = (low + high) // 2
            rowIndex = mid // n
            colIndex = mid % n
            if mat[rowIndex][colIndex] == x:
                return True
            elif mat[rowIndex][colIndex] < x:
                low = mid + 1
            else:
                high = mid - 1
                
        return False
