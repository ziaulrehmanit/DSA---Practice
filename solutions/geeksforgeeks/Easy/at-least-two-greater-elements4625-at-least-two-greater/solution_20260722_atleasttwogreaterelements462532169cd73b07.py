class Solution:
    def findElements(self,arr):
        arr.sort()
        return arr[:-2]
