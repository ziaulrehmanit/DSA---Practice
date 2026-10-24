class Solution:
    def isDistinct(self, arr):
        
        return True if len(arr) == len(set(arr)) else False
