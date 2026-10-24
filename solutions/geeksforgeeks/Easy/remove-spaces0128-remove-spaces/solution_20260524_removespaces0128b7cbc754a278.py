class Solution:
    def removeSpaces(self, s):
        result = []

        for ch in s:
            if ch != ' ':
                result.append(ch)

        return "".join(result)
