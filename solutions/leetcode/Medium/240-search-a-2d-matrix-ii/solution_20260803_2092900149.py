class Solution:
    def exists(self, arr, k):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == k:
                return True
            elif arr[mid] < k:
                low = mid + 1
            else:
                high = mid - 1
                
        return False
    
    def searchMatrix(self, mat, x):
        for i in range(len(mat)):
            if mat[i][0] <= x and x <= mat[i][len(mat[0])-1]:
                if self.exists(mat[i], x):
                    return True
        return False
