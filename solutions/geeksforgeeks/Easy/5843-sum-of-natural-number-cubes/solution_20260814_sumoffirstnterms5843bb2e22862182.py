class Solution:
    def sumOfSeries(self,n):
        sum = 1
        for i in range(2, n+1):
            sum += i ** 3
        return sum
