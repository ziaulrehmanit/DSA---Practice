class Solution:
    def rangeOfCapacity(self, weights: List[int]):
        maxi = total = 0
        for weight in weights:
            maxi = max(maxi, weight)
            total += weight
        return maxi, total
    
    def checkDays(self, weights: List[int], days: int, mid: int) -> bool:
        daysTaken, load = 1, 0
        for weight in weights:
            if weight+load > mid:
                load = weight
                daysTaken += 1
                if daysTaken > days:
                    return False
            else:
                load += weight
        return True

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = self.rangeOfCapacity(weights)
        while low <= high:
            mid = (low + high) // 2
            if self.checkDays(weights, days, mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
