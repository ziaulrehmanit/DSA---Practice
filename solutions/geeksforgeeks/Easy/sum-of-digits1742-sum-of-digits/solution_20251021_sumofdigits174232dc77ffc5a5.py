class Solution:
    def sumOfDigits(self, n):
        s=str(n)
        sumofn=0
        for i in range(len(s)):
            s1=int(s[i])
            sumofn+=s1
        return sumofn
