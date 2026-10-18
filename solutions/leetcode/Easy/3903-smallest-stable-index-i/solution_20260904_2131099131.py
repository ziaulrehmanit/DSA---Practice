class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:

        n = len(nums)
        maximum = minimum = 0

        for i in range(n):

            maximum = max(nums[0:i+1])
            minimum = min(nums[i:n])

            if (maximum - minimum) <= k:
                return i

        return -1
