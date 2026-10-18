class Solution:
    def rangeOfSum(self, arr):
        maxi = arr[0]
        total = 0
        for num in arr:
            maxi = max(maxi, num)
            total += num
        return maxi, total
    
    def checkPossible(self, arr, k, mid):
        total = 0
        count = 1
        for num in arr:
            if num+total > mid:
                count += 1
                total = num
            else:
                total += num
            if count > k:
                return False
        return True
    
    def splitArray(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return -1
        low, high = self.rangeOfSum(nums)
        while low <= high:
            mid = (low + high) // 2
            if self.checkPossible(nums, k, mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
