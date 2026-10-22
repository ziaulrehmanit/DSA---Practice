class Solution:
    def find_fact(self, n):
        
        fac = 1
        for i in range(2, n+1):
            fac *= i
            
        return fac
