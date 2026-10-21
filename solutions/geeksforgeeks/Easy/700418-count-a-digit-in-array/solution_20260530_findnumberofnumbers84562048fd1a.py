class Solution:
    def countDigitK(self, k, arr):
        
        count = 0
        
        for num in arr:
            
            temp = str(num)
            
            for j in temp:
                
                if j == str(k):
                    count += 1
                    
        return count
