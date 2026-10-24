class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        
        floor = -1
        ceil = 10000000
        
        for num in arr:
            if num <= x:
                floor = max(floor, num)
            if num >= x:
                ceil = min(ceil, num)
        
        if ceil == 10000000:
            return [floor, -1]
        return [floor, ceil]
