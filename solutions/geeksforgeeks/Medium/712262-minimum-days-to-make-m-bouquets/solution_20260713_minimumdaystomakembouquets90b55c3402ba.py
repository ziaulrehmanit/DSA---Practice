class Solution:
    def rangeOfDays(self, bloomDay):
        return min(bloomDay), max(bloomDay)

    def checkBouquets(self, bloomDay, m, k, day):
        count = bouquets = 0

        for bloom in bloomDay:
            if bloom <= day:
                count += 1
            else:
                bouquets += count // k
                count = 0

        bouquets += count // k
        return bouquets >= m

    def minDaysBloom(self, bloomDay, k, m):
        n = len(bloomDay)

        if m * k > n:
            return -1

        low, high = self.rangeOfDays(bloomDay)

        while low <= high:
            mid = (low + high) // 2

            if self.checkBouquets(bloomDay, m, k, mid):
                high = mid - 1
            else:
                low = mid + 1

        return low
