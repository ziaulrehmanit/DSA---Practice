class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        return ''.join((c * count for c, count in sorted(freq.items(), key = lambda x: x[1], reverse = True)))
