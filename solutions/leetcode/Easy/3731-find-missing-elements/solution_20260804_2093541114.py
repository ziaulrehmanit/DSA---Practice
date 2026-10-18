class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        mini = maxi = nums[0]
        for i in range(1, len(nums)):
            mini = min(mini, nums[i])
            maxi = max(maxi, nums[i])
        ans = []
        for num in range(mini, maxi+1):
            if num not in set_nums:
                ans.append(num)
        return ans
