class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        minimum=nums[0]
        maximum=nums[-1]
        missing = []
        i=1
        while(minimum<maximum):
            if i>=len(nums) or nums[i]!=minimum+1:
                missing.append(minimum+1)
            else:
                i+=1
            minimum+=1
        return missing
