class Solution:
    def sum(self, n):
        def check(k, target):
            p = (target - 1) // k
            return p * k * (p + 1) // 2
        return check(3, n) + check(7, n) - check(21, n)
