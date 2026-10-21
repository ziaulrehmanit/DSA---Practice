class Solution:
    def maxAdj(self, arr):
        
        res = []
        
        for i in range(1, len(arr)):
            
            res.append(max(arr[i], arr[i-1]))
            
        return res
