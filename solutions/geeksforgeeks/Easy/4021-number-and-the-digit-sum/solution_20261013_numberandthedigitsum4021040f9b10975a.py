class Solution:
    def numberCount(self, n, k):
        
        def digitsum(x):
            sm = 0
            while x > 0:
                sm += (x % 10)
                x //= 10
            return sm
            
        i, j = 1, n
        smallest_x = -1
        while i <= j:
            mid = (i + j)// 2
            if mid - digitsum(mid) >= k:
                smallest_x = mid
                j = mid - 1
            else:
                i = mid + 1
                
        if smallest_x == -1:
            return 0
            
        return n - smallest_x + 1
