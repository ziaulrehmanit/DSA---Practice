class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashDictionary={}
        
        for index,value in enumerate(nums):
            num=target-value
            if num in hashDictionary:
                return [hashDictionary[num],index]
            
            hashDictionary[value]=index
