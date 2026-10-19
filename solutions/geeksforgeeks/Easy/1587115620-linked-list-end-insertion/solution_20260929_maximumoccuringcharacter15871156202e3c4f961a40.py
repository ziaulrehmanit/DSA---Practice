class Solution:
    def getMaxOccuringChar(self, s):
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1
        max_cnt = 0
        res = ''
        for i in range(26):
            if freq[i] > max_cnt:
                max_cnt = freq[i]
                res = chr(i + 97)
        return res
