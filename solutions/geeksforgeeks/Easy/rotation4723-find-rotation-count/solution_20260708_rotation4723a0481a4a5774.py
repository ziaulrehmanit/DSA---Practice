class Solution:
    def findKRotation(self, arr):
        left, right = 0, len(arr)-1
        while left < right:
            mid = (left + right) // 2
            if arr[left] == arr[mid] == arr[right]:
                left += 1
                right -= 1
            elif arr[mid] > arr[right]:
                left = mid + 1
            else:
                right = mid
        return left
