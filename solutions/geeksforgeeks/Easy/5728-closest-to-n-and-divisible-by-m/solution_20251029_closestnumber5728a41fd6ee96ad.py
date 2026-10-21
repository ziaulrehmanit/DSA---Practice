class Solution:
    def closestNumber(self, n, m):
        a=int(n/m)
        n1=a*m
        if ((n*m)>0):
            n2=m*(a+1)
        else:
            n2=m*(a-1)
        if (abs(n-n1)<abs(n-n2)):
            return n1
        else:
            return n2
