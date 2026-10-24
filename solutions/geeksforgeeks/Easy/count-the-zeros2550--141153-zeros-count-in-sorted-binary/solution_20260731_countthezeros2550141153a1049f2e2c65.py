class Solution:
    def countZeroes(self, arr):
        low, high = 0, len(arr)-1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == 0:
                high = mid - 1
            else:
                low = mid + 1
        return len(arr)-low
