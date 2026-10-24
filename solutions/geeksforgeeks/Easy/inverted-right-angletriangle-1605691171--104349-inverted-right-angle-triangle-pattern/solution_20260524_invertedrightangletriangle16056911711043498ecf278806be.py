class Solution:
    def pattern(self, s):

        ans = []

        for i in range(len(s), 0, -1):
            ans.append(s[:i])

        return ans
