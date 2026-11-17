class Solution:
    def findPattern(self, s):
        cnt = 0
        prev = None
        
        for char in s:
            if char == 'x':
                if prev == 'y' and cnt != 0:
                    return False
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    return False
            prev = char
            
        return cnt == 0
