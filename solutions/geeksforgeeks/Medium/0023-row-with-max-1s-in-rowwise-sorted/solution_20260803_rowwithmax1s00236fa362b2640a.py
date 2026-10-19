class Solution:
    def lowerBound(self, arr):
        low, high = 0, len(arr)-1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == 1:
                high = mid - 1
            else:
                low = mid + 1
        return low
        
    def rowWithMax1s(self, arr):
        n = len(arr[0])
        ind = -1
        ones = 0
        for i in range(len(arr)):
            cnt = n - self.lowerBound(arr[i])
            if cnt > ones:
                ind = i
                ones = cnt
        return ind
