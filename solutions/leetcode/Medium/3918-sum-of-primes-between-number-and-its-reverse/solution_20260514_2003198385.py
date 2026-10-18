class Solution:

    def reverseNumber(self, num: int) -> int:

        res = 0

        while num > 0:
            res = (res * 10) + (num % 10)
            num //= 10

        return res

    def isPrime(self, num: int) -> bool:

        if num < 2:
            return False

        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
        
    def sumOfPrimesInRange(self, n: int) -> int:

        mavroliken = n

        r = self.reverseNumber(mavroliken)
        mini = min(mavroliken, r)
        maxi = max(mavroliken, r)
        primeSum = 0

        for i in range(mini, maxi+1):
            if self.isPrime(i):
                primeSum += i

        return primeSum
