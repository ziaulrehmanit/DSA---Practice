class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:

        if len(nums) < 3:
            return nums

        res = []
        res.insert(0, nums[0])
        k = 1
        for i in range(1, len(nums)-1):
            value = False
            j = i-1
            while j >= 0 and nums[i] > nums[j]:
                if j == 0:
                    value = True
                j -= 1
            if value == False:
                j = i+1
                while j < len(nums) and nums[i] > nums[j]:
                    if j == len(nums)-1:
                        value = True
                    j += 1
            if value:
                res.insert(k, nums[i])
                k += 1
        res.insert(k, nums[len(nums)-1])
        return res
