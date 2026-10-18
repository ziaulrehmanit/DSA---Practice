class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minimum_price = prices[0]
        maximum_profit = 0

        for i in range(1,len(prices)):

            if minimum_price > prices[i]:
                minimum_price = prices[i]

            else:
                maximum_profit = max(maximum_profit , prices[i] - minimum_price)

        return maximum_profit
