class Solution:
    def reverse(self, arr):
        
        left , right = 0 , len(arr)-1
        
        while left < right:
            
            arr[left] , arr[right] = arr[right] , arr[left]
            left += 1
            right -= 1
        
        return arr
        
    def reverseSpiral(self, R, C, a):
        
        m = len(a)
        n = len(a[0])
        left , right = 0 , n - 1
        top , bottom = 0 , m - 1
        res = []

        while top <= bottom and left <= right:

            for i in range(left, right+1):
                res.append(a[top][i])
            top += 1

            for i in range(top, bottom+1):
                res.append(a[i][right])
            right -= 1
            if top <= bottom:
                for i in range(right, left-1, -1):
                    res.append(a[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top-1, -1):
                    res.append(a[i][left])
                left += 1
        
        return self.reverse(res)
