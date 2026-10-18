class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        cnt = 0
        n = len(nums)
        for i in range(n-1):
            if nums[i] ^ nums[i+1] == 0:
                cnt += 1
        return cnt                    
