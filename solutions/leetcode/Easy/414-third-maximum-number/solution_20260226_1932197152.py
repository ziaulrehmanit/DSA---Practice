class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        Largest=secondLargest=thirdLargest=None
        for num in nums:
            if num==Largest or num==secondLargest or num==thirdLargest:
                continue
            if Largest is None or num>Largest:
                thirdLargest=secondLargest
                secondLargest=Largest
                Largest=num
            elif secondLargest is None or num>secondLargest:
                thirdLargest=secondLargest
                secondLargest=num
            elif thirdLargest is None or num>thirdLargest:
                thirdLargest=num
        if thirdLargest!=None:
            return thirdLargest
        return Largest
