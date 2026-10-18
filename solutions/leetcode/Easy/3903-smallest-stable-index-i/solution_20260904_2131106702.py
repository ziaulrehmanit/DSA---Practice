class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
            
        # Step 1: Precompute suffix minimums
        # suffix_min[i] will store min(nums[i..n-1])
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])
            
        # Step 2: Track prefix maximum on the fly and check stability
        # current_max tracks max(nums[0..i])
        current_max = nums[0]
        for i in range(n):
            current_max = max(current_max, nums[i])
            
            # Instability score: max(nums[0..i]) - min(nums[i..n-1])
            if (current_max - suffix_min[i]) <= k:
                return i
                
        return -1
