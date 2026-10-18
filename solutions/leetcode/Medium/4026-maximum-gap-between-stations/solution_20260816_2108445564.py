class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        n, m = len(skill), len(station)
        if n < 2:
            return 0
        left = [0] * n
        j = 0
        for i in range(n):
            while station[j] != skill[i]:
                j += 1
            left[i] = j
            j += 1
        right = [0] * n
        j = m - 1
        for i in range(n-1, -1, -1):
            while station[j] != skill[i]:
                j -= 1
            right[i] = j
            j -= 1
        gap = 0
        for i in range(n-1):
            gap = max(gap, right[i+1] - left[i])
        return gap
