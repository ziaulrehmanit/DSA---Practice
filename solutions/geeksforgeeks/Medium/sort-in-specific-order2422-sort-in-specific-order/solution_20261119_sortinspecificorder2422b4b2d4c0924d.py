class Solution:
    def sortIt(self, arr):
        for i, val in enumerate(arr):
            if val & 1:
                arr[i] = -val
        arr.sort()
        for i, val in enumerate(arr):
            if val < 0:
                arr[i] = -val
