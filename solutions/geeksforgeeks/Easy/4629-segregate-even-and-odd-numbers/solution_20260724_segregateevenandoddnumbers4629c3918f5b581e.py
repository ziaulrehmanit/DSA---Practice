class Solution:
    def segregateEvenOdd(self,arr):
        left = 0
        right = len(arr)-1
        while left <= right:
            if arr[left]%2 == 1:
                arr[left], arr[right] = arr[right], arr[left]
                right -= 1
            else:
                left += 1
        arr[:left] = sorted(arr[:left])
        arr[left:] = sorted(arr[left:])
