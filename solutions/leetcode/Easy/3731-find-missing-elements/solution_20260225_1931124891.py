class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        nums_set = set(nums)
        min_num = min(nums)
        max_num = max(nums)
        for num in range(min_num, max_num + 1):
            if num not in nums_set:
                ans.append(num)
        return ans
