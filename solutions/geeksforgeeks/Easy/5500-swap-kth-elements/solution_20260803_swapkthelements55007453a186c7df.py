class Solution:
    def swapKth(self, arr, k):
        arr[k-1], arr[len(arr)-k] = arr[len(arr)-k], arr[k-1]
