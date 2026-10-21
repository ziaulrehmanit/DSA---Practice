class Solution:
    def NthTerm(self, n):
        
        mod = 10**9 + 7
        if n == 1:
            return 2
        
        res = 2
        
        for i in range(2, n+1):
            res = (res * i + 1) % mod
            
        return res
