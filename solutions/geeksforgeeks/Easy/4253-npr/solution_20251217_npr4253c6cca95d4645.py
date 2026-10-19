class Solution:
    def nPr(self, n, r):
        r=n-r
        fac_of_n=1
        fac_of_r=1
        for x in range(2,n+1):
            if x<=r:
                fac_of_r*=x
            fac_of_n*=x
        return int(fac_of_n/fac_of_r)
