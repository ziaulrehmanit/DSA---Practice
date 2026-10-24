class Solution:
    def getOddOccurrence(self, arr):
        
        number=0
        for num in arr:
            number^=num
        return number
