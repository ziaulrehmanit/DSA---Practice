class Solution:
    def checkElements(self, start, end, arr):
        value = start
        for i in range(len(arr)):
            if value not in arr:
                return False
            else:
                value += 1
            if value > end:
                return True
