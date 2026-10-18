class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        max_len = float('-inf')
        for i in range(n):
            length = 0
            for j in range(i, n):
                if s[i : j+1] == s[i : j+1][::-1]:
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        res = s[i : j+1]
        return res
