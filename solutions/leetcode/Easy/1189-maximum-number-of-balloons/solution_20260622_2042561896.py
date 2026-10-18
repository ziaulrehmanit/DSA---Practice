class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        b = a = l = o = n = 0

        for char in text:
            if char == 'b':
                b += 1
            elif char == 'a':
                a += 1
            elif char == 'l':
                l += 1
            elif char == 'o':
                o += 1
            elif char == 'n':
                n += 1

        count = 0
        
        while b > 0 and a > 0 and l > 1 and o > 1 and n > 0:
            b -= 1
            a -= 1
            l -= 2
            o -= 2
            n -= 1
            count += 1
        
        return count
