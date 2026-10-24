from math import factorial
class Solution:
    def prefixStrings(self, n: int) -> int:
        mod = 10 ** 9 + 7
        numerator = factorial(2 * n)
        denumerator = factorial(n + 1) * factorial(n)
        return (numerator // denumerator) % mod
