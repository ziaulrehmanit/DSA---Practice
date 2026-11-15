class Solution:
    def twoSum(self, nums, target):
        HashMap = {}
        for i in range(len(nums)):
            n = target - nums[i]
            if n in HashMap:
                return [HashMap[n], i]
            else:
                HashMap[nums[i]] = i
        
