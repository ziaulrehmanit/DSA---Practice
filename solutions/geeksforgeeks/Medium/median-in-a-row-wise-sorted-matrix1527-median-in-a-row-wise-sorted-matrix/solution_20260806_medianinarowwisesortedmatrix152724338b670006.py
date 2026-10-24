from bisect import bisect_right

class Solution:
    def median(self, mat):
        
        n, m = len(mat), len(mat[0])
        low = min(row[0] for row in mat)
        high = max(row[-1] for row in mat)
        desired = (n * m) // 2
        while low <= high:
            count = 0
            mid = (low + high) // 2
            for row in mat:
                count += bisect_right(row, mid)
            if count <= desired:
                low = mid + 1
            else:
                high = mid - 1
        return low
