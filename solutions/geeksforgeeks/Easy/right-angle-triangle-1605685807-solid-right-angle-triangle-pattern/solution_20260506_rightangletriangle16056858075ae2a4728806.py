class Solution:
    def printTriangle(self, N):
        
        for i in range(1, N+1):
            
            if i % 2 == 0:
                value = 0
            else:
                value = 1
                
            for j in range(i):
                
                value = 1 if value%2!=0 else 0
                print(value, end = ' ')
                value -= 1
                
            print()
