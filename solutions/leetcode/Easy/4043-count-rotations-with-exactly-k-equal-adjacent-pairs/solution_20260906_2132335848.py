class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n = len(s)
        cnt = 0
        for i in range(n):
            if s[i] == s[(i + 1) % n]:
                cnt += 1
        if k == cnt:
            return n- cnt
        elif k == cnt - 1:
            return cnt
        else:
            return 0
