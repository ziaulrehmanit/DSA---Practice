class Solution:
    def leaders(self, arr):
        
        ans = []
        maxi = -1
        n = len(arr)
        
        for i in range(n-1, -1, -1):
            
            if arr[i] >= maxi:
                maxi = arr[i]
                ans.append(arr[i])
                
        start = 0
        end = len(ans) - 1
        
        while start < end:
            ans[start] , ans[end] = ans[end] , ans[start]
            start += 1
            end -= 1
            
        return ans
