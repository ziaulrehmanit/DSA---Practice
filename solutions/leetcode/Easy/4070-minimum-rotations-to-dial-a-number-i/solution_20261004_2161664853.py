class Solution:
    def minRotations(self, s: str) -> int:

        rotations = 0
        curr = 0

        for ch in s:
            target = int(ch)
            diff = abs(target - curr)

            rotations += min(diff, 10 - diff)
            curr = target

        return rotations
