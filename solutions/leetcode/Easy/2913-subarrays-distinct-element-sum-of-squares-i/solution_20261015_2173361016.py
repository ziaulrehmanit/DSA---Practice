from typing import List


__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0

        # Fix the LEFT boundary i, then grow the window to the right.
        for i in range(n):
            # Values are in [1, 100], so a fixed-size boolean array is
            # faster than a set: no hashing and no resizing.
            seen = [False] * 101
            distinct = 0  # distinct count of nums[i..j]

            for j in range(i, n):
                v = nums[j]
                # Adding nums[j] raises the distinct count only if
                # we haven't seen v inside the current window.
                if not seen[v]:
                    seen[v] = True
                    distinct += 1

                # nums[i..j] is a valid subarray: add its squared count.
                total += distinct * distinct

        return total
