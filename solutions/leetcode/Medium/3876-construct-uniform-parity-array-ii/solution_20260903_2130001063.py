class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        if not nums:
            return True
        mini = min(nums)
        if mini % 2 == 1:
            return True
        anyOdd = any(num % 2 == 1 for num in nums)
        return not anyOdd
