class Solution:
    def snakeCase(self, s: str) -> str:
        return ''.join('_' if ch is ' ' else (chr(ord(ch) ^ 32) if 65 <= ord(ch) <= 90 else ch) for ch in s)
