import bisect
class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        m = len(intervals)
        arr = sorted([inv[0] for inv in intervals])
        pairs = m * (m - 1) // 2
        cnt = 0
        for start, end in intervals:
            ind = bisect.bisect_right(arr, end)
            cnt += (m - ind)
        return pairs - cnt
