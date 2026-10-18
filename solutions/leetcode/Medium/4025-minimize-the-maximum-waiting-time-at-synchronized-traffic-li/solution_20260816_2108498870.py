class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        def check(mid):
            max_green = max(lights)
            for arrival in arrivalTime:
                r = arrival % period
                if r < max_green:
                    continue
                wait = period - r
                if wait > mid:
                    return False
            return True
        low, high = 0, period-1
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
