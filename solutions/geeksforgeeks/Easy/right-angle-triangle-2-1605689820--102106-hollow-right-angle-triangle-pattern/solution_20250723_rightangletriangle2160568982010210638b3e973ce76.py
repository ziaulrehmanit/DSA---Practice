class Solution:
    def printPattern(self, n):
        #Code here
        for i in range(1,n+1):
            for j in range(1,i+1):
                if j==i or j==1 or i==n:
                    print('* ',end="")
                else:
                    print('  ',end="")
            print()
