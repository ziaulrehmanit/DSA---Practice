class Solution:
    def swapTriangle(self,N,A):
        
        n = len(A)

        for i in range(n):
            for j in range(i+1, n):
                A[i][j] , A[j][i] = A[j][i] , A[i][j]
                
        return A
