class Solution:
    def printTriangle(self, N):
        
        for i in range(N, 0, -1):
            
            value = 65
            for j in range(i):
                print(chr(value), end = '')
                value += 1
            print()
