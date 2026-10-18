class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}
        for ind, num in enumerate(nums):
            if num in seen and ind - seen[num] <= k:
                return True
            seen[num] = ind
        return False
