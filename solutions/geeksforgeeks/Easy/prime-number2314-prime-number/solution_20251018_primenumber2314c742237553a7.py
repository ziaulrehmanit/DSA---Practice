class Solution:
    def isPrime(self, n):
        if n<2:
            return False 
        else:
            Prime=True
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    Prime=False
                    break
        return Prime           
