class Solution:
    def mergeArrays(self, a, b):
        
        left = len(a) - 1
        right = 0
        
        while left >= 0 and right < len(b):
            if a[left] > b[right]:
                temp = a[left]
                a[left] = b[right]
                b[right] = temp
            left -= 1
            right += 1
            
        a.sort()
        b.sort()
