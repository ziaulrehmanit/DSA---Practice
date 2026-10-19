class Solution:
    def isConsonant(self, c):
        return c.isalpha() and c.lower() not in "aeiou"
        
    def remConsonants(self, s):
        arr = list(s)
        result = []

        for ch in arr:
            if not self.isConsonant(ch):
                result.append(ch)

        return "".join(result)
