class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        HashMap = [0] * (n+1)
        for num in nums:
            HashMap[num] += 1
        res = []
        for i in range(1, n+1):
            if HashMap[i] == 0:
                res.append(i)
        return res
