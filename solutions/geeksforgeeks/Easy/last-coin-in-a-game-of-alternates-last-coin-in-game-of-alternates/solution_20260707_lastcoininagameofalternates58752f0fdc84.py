class Solution:
    def coin(self, arr):
        left, right = 0, len(arr) - 1

        while left < right:
            if arr[left] >= arr[right]:
                left += 1      # Remove the left coin
            else:
                right -= 1     # Remove the right coin

        return arr[left]
