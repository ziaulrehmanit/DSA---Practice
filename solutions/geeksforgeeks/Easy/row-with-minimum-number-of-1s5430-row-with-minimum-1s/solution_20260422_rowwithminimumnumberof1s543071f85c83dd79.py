class Solution:
    def minRow(self,a):
        
        n = len(a)
        m = len(a[0])
        mini_1s = 1001
        ind = 1
        
        for i in range(n):
            mini = 0
            for j in range(m):
                if a[i][j] == 1:
                    mini += 1
            if mini_1s > mini:
                mini_1s = mini
                ind = i+1
            
        return ind
