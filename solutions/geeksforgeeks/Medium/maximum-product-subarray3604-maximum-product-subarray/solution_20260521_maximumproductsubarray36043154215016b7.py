class Solution:
    def maxProduct(self,arr):
        
        maxi = float('-inf')
        prefix = suffix = 1
        
        for i in range(len(arr)):
            
            if prefix == 0:
                prefix = 1
                
            if suffix == 0:
                suffix = 1
                
            prefix *= arr[i]
            suffix *= arr[len(arr)-i-1]
            
            maxi = max(maxi, max(prefix, suffix))
            
        return maxi
