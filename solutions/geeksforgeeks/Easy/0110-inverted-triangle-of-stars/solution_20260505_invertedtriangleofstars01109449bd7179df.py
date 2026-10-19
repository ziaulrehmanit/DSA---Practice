class Solution:
    def printTriangle(self, N):
        
        stars = (N * 2) - 1
        spaces = 1
        
        for i in range(N):
            if i!=0:
                print(' ' * spaces, end = '')
                spaces += 1
            print('*' * stars, end = '\n')
            stars -= 2
