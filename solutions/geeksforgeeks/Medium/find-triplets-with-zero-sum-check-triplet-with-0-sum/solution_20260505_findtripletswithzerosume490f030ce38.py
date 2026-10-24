class Solution:
    def findTriplets(self, arr):
        
        arr.sort()
        n = len(arr)
        
        for i in range(n-2):
            
            if i > 0 and arr[i] == arr[i-1]:
                continue
            
            if arr[i] + arr[i+1] + arr[i+2] > 0:
                break
            
            if arr[i] + arr[n-1] + arr[n-2] < 0:
                continue
            
            j = i+1
            k = n-1
            
            while j < k:
                
                total = arr[i] + arr[j] + arr[k]
                
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    return True
                    
        return False
