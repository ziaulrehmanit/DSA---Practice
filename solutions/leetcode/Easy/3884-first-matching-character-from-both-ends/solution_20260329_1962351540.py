class Solution:
    def firstMatchingIndex(self, s: str) -> int:

        n = len(s)

        if n<2:
            return 0

        for i in range(n-1):

            if s[i] == s[n-i-1]:
                return i

        return -1
