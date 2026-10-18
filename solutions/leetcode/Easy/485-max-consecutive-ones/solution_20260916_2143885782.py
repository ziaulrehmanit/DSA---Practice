class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = ones = 0
        for num in nums:
            if num == 1:
                ones += 1
            else:
                maxi = max(maxi, ones)
                ones = 0
        return max(maxi, ones)
