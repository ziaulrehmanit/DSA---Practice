class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        HashDictionary = {}
        max_length = -1
        left = 0
        for right in range(n):
            HashDictionary[nums[right]] = HashDictionary.get(nums[right], 0) + 1

            while HashDictionary[nums[right]] > k:
                HashDictionary[nums[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
