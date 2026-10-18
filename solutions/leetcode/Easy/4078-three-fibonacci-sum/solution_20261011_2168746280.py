class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        a = 0
        b = 1
        c = 1
        sum = a + b + c
        while sum <= n:
            if sum == n:
                return True
            a, b, c = b, c, b + c
            sum = a + b + c
        return False
