from math import ceil
class Solution:
    def totalHours(self, piles, h, mid):
        total = 0
        for bananas in piles:
            total += ceil(bananas/mid)
            if total > h:
                return total
        return total
    
    def kokoEat(self, piles: list[int], h: int) -> int:
        low, high = 1, max(piles)
        while low <= high:
            mid = (low + high) // 2
            hours = self.totalHours(piles, h, mid)
            if hours <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low
