class Solution:
    def rangeOfPages(self, arr):
        maxi = arr[0]
        total = 0
        for num in arr:
            maxi = max(maxi, num)
            total += num
        return maxi, total
    
    def checkPossible(self, arr, k, mid):
        pages = 0
        count = 1
        for book in arr:
            if pages+book > mid:
                count += 1
                pages = book
            else:
                pages += book
            if count > k:
                return False
        return True
    
    def findPages(self, arr, k):
        if len(arr) < k:
            return -1
        low, high = self.rangeOfPages(arr)
        while low <= high:
            mid = (low + high) // 2
            if self.checkPossible(arr, k, mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
