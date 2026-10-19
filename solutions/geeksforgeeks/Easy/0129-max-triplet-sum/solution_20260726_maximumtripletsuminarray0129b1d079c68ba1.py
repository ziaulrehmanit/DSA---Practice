class Solution:
    def maxTripletSum(self, arr):
        max1 = max2 = max3 = float('-inf')
        for num in arr:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
        return max1+max2+max3
