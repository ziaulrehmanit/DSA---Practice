class Solution:
    def printTriangle(self, N):
        
        value = 65
        
        for i in range(N):
            
            for j in range(i+1):
                
                print(chr(value), end = '')
                
            print()
            
            value += 1
