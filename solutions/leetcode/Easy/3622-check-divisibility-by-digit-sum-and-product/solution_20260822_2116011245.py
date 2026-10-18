class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum, product = 0, 1
        x = n
        while x > 0:
            digit = x % 10
            sum += digit
            product *= digit
            x //= 10
        return True if n % (sum + product) == 0 else False
