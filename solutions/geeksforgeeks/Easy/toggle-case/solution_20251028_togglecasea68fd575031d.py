class Solution:
    def toggleCase(self, s):
        res=""
        for j in range(len(s)):
            if s[j].isupper():
                res+=s[j].lower()
            else:
                res+=s[j].upper()
        return res
