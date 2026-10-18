class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hash={}
        for index,value in enumerate(nums):
            num=target-value
            if num in Hash:
                return [Hash[num],index]
            Hash[value]=index
