class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = nums[0]
        n = len(nums)
        for i in range(1, n):
            ans += nums[i]
            nums[i] = ans
        return nums
