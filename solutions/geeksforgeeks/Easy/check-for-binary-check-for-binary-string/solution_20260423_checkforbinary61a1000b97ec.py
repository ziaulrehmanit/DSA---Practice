class Solution:
    def isBinary(self, s):
        
        for char in s:
            if char != "0" and char != "1":
                return False
        return True
