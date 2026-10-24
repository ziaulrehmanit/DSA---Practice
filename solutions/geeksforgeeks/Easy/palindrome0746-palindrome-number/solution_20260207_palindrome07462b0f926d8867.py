class Solution:
    def isPalindrome(self, n):
        
        if n<0:
            return False
        original=n
        rev=0
        while n>0:
            rev=rev*10+(n%10)
            n=n//10
        if original!=rev:
            return False
        return True
