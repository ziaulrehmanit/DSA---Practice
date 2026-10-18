class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini = maxi = nums[0]
        for num in nums:
            mini = min(mini, num)
            maxi = max(maxi, num)
        while maxi != 0:
            mini, maxi = maxi, mini%maxi
        return mini
