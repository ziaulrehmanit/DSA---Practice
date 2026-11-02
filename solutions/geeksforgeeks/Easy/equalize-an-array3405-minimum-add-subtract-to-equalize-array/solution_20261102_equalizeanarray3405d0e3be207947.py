class Solution:
    def equalizeArray(self, arr, k):
        
        rem = arr[0] % k
        for num in arr:
            if rem != num % k:
                return -1
                
        arr.sort()
        median = arr[len(arr) // 2]
        
        return sum(abs(median - num) for num in arr) // k
