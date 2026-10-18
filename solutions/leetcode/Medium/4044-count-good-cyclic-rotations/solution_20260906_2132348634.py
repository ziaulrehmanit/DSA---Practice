class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        cnt = 0
        n = len(nums)
        total = sum(nums)
        half = n // 2
        first = sum(nums[:half])
        for i in range(n):
            second = total - first
            if first > second:
                cnt += 1
            first += nums[(i + half) % n] - nums[i]
        return cnt
