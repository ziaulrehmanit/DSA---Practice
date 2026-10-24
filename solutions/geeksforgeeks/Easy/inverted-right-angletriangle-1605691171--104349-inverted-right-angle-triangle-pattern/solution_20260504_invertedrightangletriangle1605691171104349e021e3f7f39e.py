class Solution:
    def printTriangle(self, N):
        
        n = N
        for i in range(1, N+1):
            for j in range(1, n+1):
                print(j, end=' ')
            n -= 1
            print()
