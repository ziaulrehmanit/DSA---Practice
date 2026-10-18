class Solution:
    def checkRoman(self, s: str, ch: chr, i: int) -> tuple[int, int]:

        if ch == 'I':
            return 1, i
        elif ch == 'V':
            if i !=0 and s[i-1] == 'I':
                return 4, i - 1
            return 5, i
        elif ch == 'X':
            if i !=0 and s[i-1] == 'I':
                return 9, i - 1
            return 10, i
        elif ch == 'L':
            if i !=0 and s[i-1] == 'X':
                return 40, i - 1
            return 50, i
        elif ch == 'C':
            if i !=0 and s[i-1] == 'X':
                return 90, i - 1
            return 100, i
        elif ch == 'D':
            if i !=0 and s[i-1] == 'C':
                return 400, i - 1
            return 500, i
        elif ch == 'M':
            if i !=0 and s[i-1] == 'C':
                return 900, i - 1
            return 1000, i
        
    def romanToInt(self, s: str) -> int:
        
        n, i = 0, len(s)-1
        while i >= 0:
            a, b = self.checkRoman(s, s[i], i)
            n += a
            i = b - 1
        return n
