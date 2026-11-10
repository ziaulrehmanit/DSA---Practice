class Solution:
    def firstElementKTime(self, arr: list[int], k: int) -> int:
        counts = {}

        for num in arr:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] == k:
                return num

        return -1
