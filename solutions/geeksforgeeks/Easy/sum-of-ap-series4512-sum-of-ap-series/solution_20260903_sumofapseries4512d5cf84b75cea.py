class Solution:
    def sumOfAP(self, n, a, d):
        sum = a
        for i in range(2, n+1):
            sum += (a + (i - 1) * d)
        return sum
