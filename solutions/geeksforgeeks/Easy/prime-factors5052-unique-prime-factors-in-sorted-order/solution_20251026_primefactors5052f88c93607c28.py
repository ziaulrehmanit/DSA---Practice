class Solution:
    def isPrime(self, n):
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(n**0.5) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    def primeFac(self, n):
        if n <= 1:
            return []

        divisors = []
        # Check for factor 2
        if n % 2 == 0:
            divisors.append(2)
            while n % 2 == 0:
                n //= 2

        # Check odd factors
        i = 3
        while i * i <= n:
            if n % i == 0:
                divisors.append(i)
                while n % i == 0:
                    n //= i
            i += 2

        # If remaining n is prime
        if n > 2:
            divisors.append(n)

        return divisors
