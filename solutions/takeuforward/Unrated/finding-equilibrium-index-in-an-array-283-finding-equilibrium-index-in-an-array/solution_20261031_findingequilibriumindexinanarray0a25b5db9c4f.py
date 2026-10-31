class Solution:
    def equilibriumIndex(self, nums):
        total_sum = sum(nums)
        left_sum = 0
        
        for i in range(len(nums)):
            # The right sum is the total sum minus the left sum minus the current element
            right_sum = total_sum - left_sum - nums[i]
        
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
            
        return -1
