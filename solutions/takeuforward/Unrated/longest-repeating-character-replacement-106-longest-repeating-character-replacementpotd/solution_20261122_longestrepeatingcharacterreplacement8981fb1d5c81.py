class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        left = max_freq = 0

        for right, char in enumerate(s):
            index = ord(char) - 65
            count[index] += 1
            max_freq = max(max_freq, count[index])

            if (right - left + 1) - max_freq > k:
                count[ord(s[left]) - 65] -= 1
                left += 1

        return len(s) - left
