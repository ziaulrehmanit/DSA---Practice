class Solution:
    def canWePlace(self, arr, k, mid):
        count, last = 1, arr[0]
        for i in range(1, len(arr)):
            if arr[i] - last >= mid:
                count += 1
                last = arr[i]
            if count >= k:
                return True
        return False
    def aggressiveCows(self, arr, k):
        arr.sort()
        low , high = 1, arr[-1]-arr[0]
        while low <= high:
            mid = (low + high) // 2
            if self.canWePlace(arr, k, mid):
                low = mid + 1
            else:
                high = mid - 1
        return high
