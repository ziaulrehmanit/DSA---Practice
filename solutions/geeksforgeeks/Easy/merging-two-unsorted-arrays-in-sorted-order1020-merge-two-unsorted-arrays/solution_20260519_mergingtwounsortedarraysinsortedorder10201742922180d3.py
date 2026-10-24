class Solution:
    def sortedMerge(self, arr1,arr2,res):
        
        arr1.sort()
        arr2.sort()
        
        ans = [] 
        
        left = 0
        right = 0
        
        m = len(arr1)
        n = len(arr2)
        
        while left < m and right < n:
            if arr1[left] <= arr2[right]:
                ans.append(arr1[left])
                left += 1
            else:
                ans.append(arr2[right])
                right += 1
                
        while left < m:
            ans.append(arr1[left])
            left += 1
            
        while right < n:
            ans.append(arr2[right])
            right += 1
            
        for i in range(m+n):
            res[i] = ans[i]
        
