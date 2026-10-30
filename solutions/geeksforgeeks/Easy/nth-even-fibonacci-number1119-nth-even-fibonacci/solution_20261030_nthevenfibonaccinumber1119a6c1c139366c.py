class Solution:
    def nthEvenFibonacci(self, n):
        if n == 1:
            return 2
        if n == 2:
            return 8

        prev2 = 2  # E_1
        prev1 = 8  # E_2

        for _ in range(3, n + 1):
            current = 4 * prev1 + prev2
            prev2 = prev1
            prev1 = current

        return prev1
