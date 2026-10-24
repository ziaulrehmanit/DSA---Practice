class Solution:
    def longest(self, arr):
        
        maxi = arr[0]
        
        for i in range(len(arr)):
            
            if len(maxi) < len(arr[i]):
                maxi = arr[i]
                
        return maxi
