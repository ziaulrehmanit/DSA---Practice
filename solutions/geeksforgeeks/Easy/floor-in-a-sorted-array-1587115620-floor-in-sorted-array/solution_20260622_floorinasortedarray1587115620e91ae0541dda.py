class Solution:
    def findFloor(self, arr, x):
        
        start = 0
        end = len(arr)-1
        ans = -1
        
        while start <= end:
            
            mid = (start + end) // 2
            
            if arr[mid] <= x:
                ans = mid
                start = mid +1
            else:
                end = mid - 1
                
        return ans
