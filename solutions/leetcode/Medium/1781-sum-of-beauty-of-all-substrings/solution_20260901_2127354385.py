class Solution:
    def beautySum(self, s: str) -> int:
        n, ans = len(s), 0
        for i in range(n):
            freq = {}
            for j in range(i, n):
                freq[s[j]] = freq.get(s[j], 0) + 1
                values = freq.values()
                ans += (max(values) - min(values))
        return ans
