class Solution:
    def maximumRowValue(self, mat, col):
        maxi = float('-inf')
        index = -1
        for row in range(len(mat)):
            if mat[row][col] > maxi:
                maxi = mat[row][col]
                index = row
        return index

    def findPeakGrid(self, mat):
        m, n = len(mat), len(mat[0])
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            row = self.maximumRowValue(mat, mid)
            curr = mat[row][mid]
            left = mat[row][mid-1] if mid-1 >= 0 else float('-inf')
            right = mat[row][mid+1] if mid+1 < n else float('-inf')
            if left <= curr and curr >= right:
                return [row, mid]
            elif left < curr:
                low = mid + 1
            else:
                high = mid - 1
