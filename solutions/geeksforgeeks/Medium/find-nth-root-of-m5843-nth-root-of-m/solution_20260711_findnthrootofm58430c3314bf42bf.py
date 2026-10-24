class Solution:
    def nthRoot(self, n, m):
        
        low, high = 0, m
        while low <= high:
            mid = (low + high) // 2
            if mid**n == m:
                return mid
            if mid**n < m:
                low = mid + 1
            else:
                high = mid - 1
        return -1
