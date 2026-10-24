class Solution:
    def findTwoElement(self, arr):
        
        n = len(arr)
        
        S = SN = 0
        S2 = S2N = 0
         
        SN = (n * (n + 1)) // 2
        S2N = (n * (n + 1) * (2 * n + 1)) // 6
        
        for i in range(n):
            S += arr[i]
            S2 += (arr[i] * arr[i])
            
        val1 = S - SN
        val2 = S2 - S2N
        val2 = val2 // val1
        
        x = (val1 + val2) // 2
        y = x - val1
        
        return [x, y]
