class Solution:
    def isPalindrome(self, n):
        s1=str(n)
        s2=s1[::-1]
        Palindrome=True
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                Palindrome=False
                break 
        return Palindrome
