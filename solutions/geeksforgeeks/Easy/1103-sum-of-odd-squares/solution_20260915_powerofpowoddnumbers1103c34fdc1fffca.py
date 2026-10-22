class Solution:
    def sumofodd(self, n: int) -> int:
        return (n * (4 * n ** 2 - 1)) // 3
