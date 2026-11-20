class Solution:
    def largestPrimeFactor(self, n):
        
        while n % 2 == 0:
            largest = 2
            n //= 2
            
        i = 3
        while i * i <= n:
            while n % i == 0:
                largest  = i
                n //= i
                
            i += 2
            
        if n > 1:
            largest = n
            
        return largest
