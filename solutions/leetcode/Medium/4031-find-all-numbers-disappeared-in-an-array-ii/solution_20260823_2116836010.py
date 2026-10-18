class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        arr_set = set(nums)
        res = []
        start = None
        for num in range(lower, upper+1):
            if num not in arr_set:
                if start is None:
                    start = num
            elif start is not None:
                res.append([start, num-1])
                start = None
        if start is not None:
            res.append([start, upper])
        return res
