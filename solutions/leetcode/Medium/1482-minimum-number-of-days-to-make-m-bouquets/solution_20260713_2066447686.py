class Solution:
    def rangeOfDays(self, bloomDay):
        mini = float('+inf')
        maxi = float('-inf')
        for days in bloomDay:
            mini = min(mini, days)
            maxi = max(maxi, days)
        return mini, maxi
    
    def checkBouquets(self, bloomDay, m, k, mid):
        count = bouquets =0
        for days in bloomDay:
            if mid >= days:
                count += 1
                if count == k:
                    bouquets += 1
                    count = 0
            else:
                count = 0
            if bouquets == m:
                return True
        return False
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k > n:
            return -1
        low, high = self.rangeOfDays(bloomDay)
        while low <= high:
            mid = (low + high) // 2
            if self.checkBouquets(bloomDay, m, k, mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
