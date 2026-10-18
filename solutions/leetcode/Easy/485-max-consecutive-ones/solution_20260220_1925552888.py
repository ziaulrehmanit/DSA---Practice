class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        ones=maxOnes=0
        for num in nums:
            if num==0:
                ones=0
            else:
                ones+=1
            if ones>maxOnes:
                maxOnes=ones
        return maxOnes
