class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        m = len(intervals)
        cnt = 0
        for i in range(m):
            for j in range(i+1, m):
                if intervals[i][1] >= intervals[j][0] and intervals[i][0] <= intervals[j][1]:
                    cnt += 1
        return cnt
