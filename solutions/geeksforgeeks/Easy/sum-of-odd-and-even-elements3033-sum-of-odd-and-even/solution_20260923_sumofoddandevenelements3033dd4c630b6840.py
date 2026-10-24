class Solution:
    def findSum(self, n):
        if n % 2 == 0:
            return [(n // 2) ** 2, (n // 2) * ((n // 2) + 1)]
        else:
            return [((n + 1) // 2) ** 2, ((n - 1) // 2) * (((n - 1) // 2) + 1)]
