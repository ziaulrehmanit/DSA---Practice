class Solution:
    def countEvenSubstr(self, s):
        cnt = 0
        for i in range(len(s)):
            if s[i] in "02468":
                cnt += i + 1
        return cnt
