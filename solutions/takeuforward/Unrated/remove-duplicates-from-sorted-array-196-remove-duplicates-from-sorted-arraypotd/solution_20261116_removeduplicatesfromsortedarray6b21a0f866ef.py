class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        ind = 1
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] != nums[i]:
                nums[ind] = nums[i]
                ind += 1
        return ind
