class Solution:
    def digitRange(self, n):
        largest = -1
        smallest = 1000000
        while n > 0:
            digit = n % 10
            largest = max(largest, digit)
            smallest = min(smallest, digit)
            n //= 10
        return largest - smallest

    def maxDigitRange(self, nums: list[int]) -> int:
        res = []
        maxRange = -1
        for num in nums:
            r = self.digitRange(num)
            maxRange = max(maxRange, r)
            res.append(r)
        sum = 0
        for i in range(len(nums)):
            if res[i] == maxRange:
                sum += nums[i]
        return sum
