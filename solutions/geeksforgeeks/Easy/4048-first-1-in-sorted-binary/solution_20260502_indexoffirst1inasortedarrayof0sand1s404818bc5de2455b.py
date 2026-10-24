class Solution:
    def firstIndex(self, arr):
        
        for num in arr:
            if num == 1:
                return arr.index(num)
        return -1
