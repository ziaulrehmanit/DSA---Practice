class Solution:
    def getMoreAndLess(self, arr, target):
        
        first = second = 0
        
        for num in arr:
            
            if num <= target:
                first += 1
            
            if num >= target:
                second += 1
                
        return [first, second]
