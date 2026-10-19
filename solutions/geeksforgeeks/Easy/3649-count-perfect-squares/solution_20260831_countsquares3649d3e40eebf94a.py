class Solution:
    def countSquares(self, n):
        cnt, sq = 0, 1
        d = 3
        while True:
            if sq < n:
                cnt += 1
                sq += d
                d += 2
            else:
                return cnt
