class Solution:
    def getSmallestDivNum(self, n):
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            
            return a
            
        ans = 1
        for i in range(2, n+1):
            ans = (i * ans) // gcd(ans, i)
            
        return ans
