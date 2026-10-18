class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        res = []
        HashMap = {}

        for num in nums:
            if num in HashMap:
                HashMap[num] += 1
            else:
                HashMap[num] = 1
        
        for value in HashMap:
            if HashMap[value] > (len(nums)//3):
                res.append(value)
                
        return res
