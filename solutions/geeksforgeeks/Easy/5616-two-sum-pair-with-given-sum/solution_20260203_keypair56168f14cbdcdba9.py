class Solution:
    def twoSum(self, arr, target):
        
        isFound=False
        hashDictionary={}
        
        for index,value in enumerate (arr):
            
            num=target-value
            if num in hashDictionary:
                isFound=True
                break
            hashDictionary[value]=index
            
        return isFound
