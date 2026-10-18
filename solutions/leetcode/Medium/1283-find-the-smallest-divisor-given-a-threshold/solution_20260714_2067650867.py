class Solution:
    def checkDivisor(self, nums, threshold, mid):
        total = 0
        for num in nums:
            total += (num + mid - 1) // mid
            if total > threshold:
                return False
        return True
    
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high = 1, max(nums)
        while low <= high:
            mid = (low + high) // 2
            if self.checkDivisor(nums, threshold, mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
