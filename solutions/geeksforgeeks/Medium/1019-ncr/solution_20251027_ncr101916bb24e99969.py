class Solution:
    def nCr(self, n, r):
        sum=1
        for j in range(1,r+1):
            sum=sum*(n-r+j)//j
        return sum   
