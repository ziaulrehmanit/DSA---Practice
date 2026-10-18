class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = ones = 0
        for num in nums:
            if num == 1:
                ones += 1
                maxi = max(maxi, ones)
            else:
                ones = 0
        return maxi
