class Solution:
    def printTriangle(self, N):
        
        stars = 1
        spaces = N - 1
        
        for i in range(N):
            if i!=N-1:
                print(' ' * spaces, end = '')
                spaces -= 1
            print('*' * stars, end = '\n')
            stars += 2
