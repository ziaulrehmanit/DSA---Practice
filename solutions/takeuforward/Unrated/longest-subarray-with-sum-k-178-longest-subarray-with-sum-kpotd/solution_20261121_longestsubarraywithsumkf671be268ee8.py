class Solution:
    def longestSubarray(self, nums, k):
        prefix_map = {}
        curr_sum = 0
        max_len = 0

        for i, num in enumerate(nums):
            curr_sum += num
            if curr_sum == k:
                max_len = i + 1
            elif curr_sum - k in prefix_map:
                max_len = max(max_len, i - prefix_map[curr_sum - k])
            if curr_sum not in prefix_map:
                prefix_map[curr_sum] = i

        return max_len
