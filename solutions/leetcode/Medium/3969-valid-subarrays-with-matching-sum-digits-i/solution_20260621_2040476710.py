class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:

        count = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                temp = str(sum)
                if temp[0] == str(x) and temp[-1] == str(x):
                    count += 1
        return count
