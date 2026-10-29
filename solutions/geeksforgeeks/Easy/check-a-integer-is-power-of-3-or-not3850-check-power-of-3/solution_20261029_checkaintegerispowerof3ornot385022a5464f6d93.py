class Solution:
    def isPowerOf3(self, n):
        if n < 0:
            return False
            
        while n % 3 == 0:
            n //= 3
            
        return n == 1
