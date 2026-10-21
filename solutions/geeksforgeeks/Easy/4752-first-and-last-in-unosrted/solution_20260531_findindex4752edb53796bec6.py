class Solution:
    def findIndex (self, arr, key):
        
        start = 0
        end = len(arr)-1
        
        while start <= end:
            
            if arr[start] == key and arr[end] == key:
                return [start, end]
            elif arr[start] == key and arr[end] != key:
                end -= 1
            elif arr[start] != key and arr[end] == key:
                start += 1
            else:
                start += 1
                end -= 1
                
        return [-1, -1]
