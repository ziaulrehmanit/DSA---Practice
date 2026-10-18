class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        n = len(chars)
        start = 0
        while start < n:
            end = start
            while end < n and chars[end] != ' ':
                end += 1
            l, r = start, end - 1
            while l < r:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1
            start = end + 1
        return "".join(chars)
