class Solution:
    def findSum(self, n):
        sum=0
        if n<0:
            sum=n*-1
        for i in range(n+1):
            sum+=i
        return sum
