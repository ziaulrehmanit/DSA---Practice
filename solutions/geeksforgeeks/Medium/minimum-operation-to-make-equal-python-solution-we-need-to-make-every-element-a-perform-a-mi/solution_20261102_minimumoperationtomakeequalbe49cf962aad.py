class Solution:
    def minOps(self, arr):
        
        n = len(arr)
        sm = mini = arr[0]
        
        for i in range(1, n):
            sm += arr[i]
            mini = min(mini, arr[i])
            
        return sm - (n * mini)
