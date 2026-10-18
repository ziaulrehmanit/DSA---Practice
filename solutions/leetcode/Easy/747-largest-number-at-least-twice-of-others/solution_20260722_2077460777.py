class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        ind = maxi = -1
        for i in range(len(nums)):
            if nums[i] > maxi:
                maxi = nums[i]
                ind = i
        for num in nums:
            if num != maxi and num*2 > maxi:
                return -1
        return ind
