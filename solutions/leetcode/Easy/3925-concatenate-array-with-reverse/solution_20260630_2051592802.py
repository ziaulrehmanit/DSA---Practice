class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        
        n = len(nums)
        res = [0] * (n * 2)

        for i in range(n):
            res[i], res[i + n] = nums[i], nums[n - i -1]

        return res
