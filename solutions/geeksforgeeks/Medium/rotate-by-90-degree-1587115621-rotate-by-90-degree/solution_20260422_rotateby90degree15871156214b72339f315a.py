class Solution:
    def rotateMatrix(self, mat):
        
        n = len(mat)

        for i in range(n):
            for j in range(i+1, n):
                mat[i][j] , mat[j][i] = mat[j][i] , mat[i][j]
                
        i = j = 0
        while i < (n // 2):
            j = 0
            while j < n:
                mat[i][j] , mat[n-1-i][j] = mat[n-1-i][j] , mat[i][j]
                j += 1
            i += 1
