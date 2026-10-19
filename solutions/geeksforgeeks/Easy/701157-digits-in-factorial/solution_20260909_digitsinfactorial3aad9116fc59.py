import math
class Solution:
    def digitsInFactorial(self,n):
        
        if n <= 1:
            return 1
        
        return int(n * math.log10(n / math.e) + math.log10(2 * math.pi * n) / 2 + 1)
