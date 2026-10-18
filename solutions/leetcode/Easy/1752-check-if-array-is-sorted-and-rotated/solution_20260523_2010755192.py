class Solution:
    def check(self, nums: List[int]) -> bool:
        
        n = len(nums)-1
        count = 0

        for i in range(n):

            if nums[i] > nums[i+1]:
                count += 1
        
        if nums[n] > nums[0]:
            count += 1

        return False if count >= 2 else True
