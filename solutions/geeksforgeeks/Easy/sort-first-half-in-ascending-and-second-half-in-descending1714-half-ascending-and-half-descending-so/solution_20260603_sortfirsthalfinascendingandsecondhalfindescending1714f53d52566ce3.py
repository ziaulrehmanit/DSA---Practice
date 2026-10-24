class Solution:
    def customSort(self, arr):
        
        n = len(arr)
        
        mid = n // 2
        
        arr[:mid] = sorted(arr[:mid])                  
        arr[mid:] = sorted(arr[mid:], reverse=True)
        
        return arr
