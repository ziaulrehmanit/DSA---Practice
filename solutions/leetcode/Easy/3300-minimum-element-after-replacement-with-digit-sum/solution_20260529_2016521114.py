class Solution:
    def minElement(self, nums: List[int]) -> int:

        mini = 100000
        
        for num in nums:

            res = 0

            while num > 0:

                res += num % 10
                num //= 10

            mini = min(mini, res)

        return mini
