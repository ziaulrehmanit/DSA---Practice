class Solution:
    def isDigitSumPalindrome(self, n):
        
        num = 0
        while n:
            num += (n % 10)
            n //= 10
        rev = 0
        dup = num
        while dup:
            rev = (rev * 10) + (dup % 10)
            dup //= 10
        return num == rev
