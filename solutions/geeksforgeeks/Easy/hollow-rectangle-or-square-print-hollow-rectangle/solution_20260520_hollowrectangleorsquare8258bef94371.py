class Solution:
    def printHollowRect(self, n, m):
        
        for i in range(n):
            
            if i == 0 or i == n-1:
                print("*" * m, end = "\n")
                continue
            
            for j in range(m):
                
                if j == 0 or j == m-1:
                    print("*", end = "")
                
                else:
                    print(" ", end = "")
                
            print()
