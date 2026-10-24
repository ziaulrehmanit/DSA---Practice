class Solution:
    def myAtoi(self, s):
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        sign, cnt_sign = 1, 0
        while i < len(s) and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            cnt_sign += 1
            if cnt_sign > 1:
                return 0
            i += 1
        num = 0
        while i < len(s) and '0' <= s[i] <= '9':
            num = num * 10 + int(s[i])
            i += 1
        num *= sign
        if num < -2147483648:
            return -2147483648
        elif num > 2147483647:
            return 2147483647
        else:
            return num
