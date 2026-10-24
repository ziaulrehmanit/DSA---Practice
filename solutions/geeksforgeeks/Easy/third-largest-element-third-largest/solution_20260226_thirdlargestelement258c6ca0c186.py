class Solution:
    def thirdLargest(self,arr):
        
        if len(arr)<3:
            return -1
        Largest=secondLargest=thirdLargest=-1
        for num in arr:
            if num>Largest:
                thirdLargest=secondLargest
                secondLargest=Largest
                Largest=num
            elif num>secondLargest:
                thirdLargest=secondLargest
                secondLargest=num
            elif num>thirdLargest:
                thirdLargest=num
        return thirdLargest
