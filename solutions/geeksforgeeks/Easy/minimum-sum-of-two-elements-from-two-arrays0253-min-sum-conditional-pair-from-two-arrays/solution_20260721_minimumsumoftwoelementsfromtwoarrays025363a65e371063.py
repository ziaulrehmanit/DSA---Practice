class Solution:
    def minSum(self, arr1, arr2):
        INF = float('inf')

        min1 = sec1 = INF
        idx1 = -1
        for i, x in enumerate(arr1):
            if x < min1:
                sec1 = min1
                min1 = x
                idx1 = i
            elif x < sec1:
                sec1 = x

        min2 = sec2 = INF
        idx2 = -1
        for i, x in enumerate(arr2):
            if x < min2:
                sec2 = min2
                min2 = x
                idx2 = i
            elif x < sec2:
                sec2 = x

        if idx1 != idx2:
            return min1 + min2

        return min(min1 + sec2, sec1 + min2)
