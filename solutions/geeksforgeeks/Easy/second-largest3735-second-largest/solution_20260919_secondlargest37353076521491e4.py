class Solution:
    def getSecondLargest(self, arr):
        max1 = max2 = -1
        for num in arr:
            if num > max1:
                max2 = max1
                max1 = num
            elif num != max1 and num > max2:
                max2 = num
        return max2
