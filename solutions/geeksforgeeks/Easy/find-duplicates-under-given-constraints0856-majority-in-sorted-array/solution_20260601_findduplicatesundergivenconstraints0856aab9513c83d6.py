class Solution:
    def isMajority(self, arr):
        
        count = 0
        
        for num in arr:
            
            if count == 0:
                value = num
            
            if num == value:
                count += 1
            else:
                count -= 1
                
        count = 0
        for num in arr:
            
            if value == num:
                count += 1
                
        return True if count>(len(arr)//2) else False
