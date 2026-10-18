class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        
        price = 0
        count = 0

        cost.sort()

        i = len(cost) - 1

        while i >= 0:

            if count == 2:
                count = 0
            else:
                price += cost[i]
                count += 1

            i -= 1

        return price
