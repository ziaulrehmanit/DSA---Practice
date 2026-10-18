class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort()
        discounts.sort()
        i, j = len(prices)-1, len(discounts)-1
        while i >= 0 and j >= 0:
            prices[i] = (prices[i] * (100 - discounts[j])) / 100
            i -= 1
            j -= 1
        sum = 0
        for price in prices:
            sum += price
        return float(f"{sum:.5f}")
