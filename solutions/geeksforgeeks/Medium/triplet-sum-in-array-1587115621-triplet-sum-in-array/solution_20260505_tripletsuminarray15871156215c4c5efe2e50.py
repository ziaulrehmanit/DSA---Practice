class Solution:
    def hasTripletSum(self, arr, target):
        
        arr.sort()
        n = len(arr)
        
        for i in range(n-2):
            
            if i > 0 and arr[i] == arr[i-1]:
                continue
            
            if arr[i] + arr[i+1] + arr[i+2] > target:
                break
            
            if arr[i] + arr[n-1] + arr[n-2] < target:
                continue
            
            j = i+1
            k = n-1
            
            while j < k:
                
                total = arr[i] + arr[j] + arr[k]
                
                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                else:
                    return True
                    
        return False
