class Solution:
    def maxSubarraySum(self, arr):
        
        maxi = float('-inf')
        sum = 0

        for num in arr:

            sum += num

            if sum > maxi:
                maxi = sum

            if sum < 0:
                sum = 0

        return maxi
