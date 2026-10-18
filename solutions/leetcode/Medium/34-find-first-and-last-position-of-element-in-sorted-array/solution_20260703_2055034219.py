class Solution:
    def firstPosition(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        ans = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                ans = mid
                end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return ans
    def lastPosition(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        ans = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                ans = mid
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return ans
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.firstPosition(nums, target), self.lastPosition(nums, target)]
