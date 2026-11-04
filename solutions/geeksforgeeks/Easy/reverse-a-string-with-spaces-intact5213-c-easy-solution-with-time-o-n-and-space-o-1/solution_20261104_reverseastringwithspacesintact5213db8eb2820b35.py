class Solution:
    def reverses(self, s):
        arr = list(s)
        i, j = 0, len(arr)-1
        while i < j:
            if arr[i] == ' ':
                i += 1
                continue
            
            if arr[j] == ' ':
                j -= 1
                continue
            
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            
        return ''.join(arr)
