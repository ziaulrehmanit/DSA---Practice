class Solution:
    def removeOuter(self, s):
        level = 0
        result = ""
        for char in s:
            if char == '(':
                if level > 0:
                    result += char
                level += 1
            elif char == ')':
                level -= 1
                if level > 0:
                    result += char
        return result
