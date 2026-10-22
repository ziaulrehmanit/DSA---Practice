class Solution:
    def searchMatrix(self,matrix, x):
        
        
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            
            for j in range(m):
                
                if matrix[i][j] == x:
                    return True
                
        return False
