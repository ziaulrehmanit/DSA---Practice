class Solution:
    def countOnes(self, arr):
        low, high = 0, len(arr)-1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == 1:
                low = mid + 1
            else:
                high = mid - 1
        return low
