class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        unique = set(candyType)
        return min(len(unique), len(candyType) // 2)
