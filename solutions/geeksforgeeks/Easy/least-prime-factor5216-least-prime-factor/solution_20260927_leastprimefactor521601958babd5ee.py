class Solution:
    def leastPrimeFactor (self, n):
        arr = [0] * (n + 1)
        arr[1] = 1
        for i in range(2, n+1):
            if arr[i] == 0:
                arr[i] = i
                
                for j in range(i * 2, n+1, i):
                    if arr[j] == 0:
                        arr[j] = i
                        
        return arr
