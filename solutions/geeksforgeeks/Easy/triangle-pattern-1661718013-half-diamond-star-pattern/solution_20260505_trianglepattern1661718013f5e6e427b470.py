class Solution:
    def printTriangle(self, n):
        
        stars = 1
        
        while stars <= n:
            print('* ' * stars, end = '\n')
            stars += 1
            
        stars -= 2
        
        while stars > 0:
            print('* ' * stars, end = '\n')
            stars -= 1
