class Solution:
    
    def getSingle(self,arr):
        
        unique=0
        for num in arr:
            unique^=num
        return unique
