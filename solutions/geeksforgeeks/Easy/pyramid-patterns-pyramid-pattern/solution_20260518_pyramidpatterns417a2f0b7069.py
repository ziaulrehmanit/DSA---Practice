class Solution:
    def printPyramid(self, n):
        
        spaces = n - 1
        stars = 1
        
        for i in range(n):
            
            print(" " * spaces, end = "")
            spaces -= 1
            
            print("*" * stars)
            stars += 2
