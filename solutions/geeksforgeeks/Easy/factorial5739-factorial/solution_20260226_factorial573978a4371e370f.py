class Solution:
    def factorial(self, n: int) -> int:
        
        fac=1
        for i in range(2,n+1):
            fac*=i
        return fac
