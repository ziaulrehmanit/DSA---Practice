class Solution:
    def checkSpy(self, n):
        
        s, p = 0, 1
        while n:
            d = n % 10
            
            #If any digit is 0, product = 0
            #Any number > 0 with digit 0 have sum == 0
            if d == 0:
                return False
                
            s += d
            p *= d
            n //= 10
            
        return s == p
