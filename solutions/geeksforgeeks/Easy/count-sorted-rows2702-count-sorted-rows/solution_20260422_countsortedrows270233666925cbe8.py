class Solution:
    def sortedCount(self,N,M,Mat):
        
        res = 0
        
        for i in range(N):
            inc = dec  = True 
            for j in range(1, M):
                if Mat[i][j] <= Mat[i][j-1]:
                    inc = False
                if Mat[i][j] >= Mat[i][j-1]:
                    dec = False
            if inc or dec:
                res += 1
               
        return res
