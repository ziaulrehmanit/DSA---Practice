class Solution:
    def countSubarray(self, arr: list[int], l: int, r: int) -> int:

        def count_at_most(k):
            left = 0
            total = 0
            cnt = 0

            for right in range(len(arr)):
                total += arr[right]

                while total > k:
                    total -= arr[left]
                    left += 1

                cnt += right - left + 1

            return cnt

        return count_at_most(r) - count_at_most(l - 1)
