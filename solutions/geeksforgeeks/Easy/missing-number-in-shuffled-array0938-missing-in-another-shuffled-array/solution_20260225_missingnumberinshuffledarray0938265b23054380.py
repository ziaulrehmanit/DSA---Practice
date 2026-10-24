class Solution:
    def findMissing(self, arr1,arr2):
        
        number=0
        for num in arr1:
            number^=num
        for num in arr2:
            number^=num
        return number
