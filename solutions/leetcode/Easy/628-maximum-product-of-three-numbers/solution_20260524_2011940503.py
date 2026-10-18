class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        maxi1 = maxi2 = maxi3 = float('-inf')
        mini1 = mini2 = float('+inf')

        for num in nums:

            if num > maxi1:

                maxi3 = maxi2
                maxi2 = maxi1
                maxi1 = num

            elif num > maxi2:

                maxi3 = maxi2
                maxi2 = num

            elif num > maxi3:

                maxi3 = num

            if num < mini1:

                mini2 = mini1
                mini1 = num

            elif num < mini2:

                mini2 = num

        return max(maxi1 * maxi2 * maxi3, mini1 * mini2 * maxi1)
