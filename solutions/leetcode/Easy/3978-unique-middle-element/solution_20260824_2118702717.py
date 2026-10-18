class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n = len(nums)
        mid = n // 2
        for i in range(mid-1, -1, -1):
            if nums[mid] == nums[i]:
                return False
        for i in range(mid+1, n):
            if nums[mid] == nums[i]:
                return False
        return True
