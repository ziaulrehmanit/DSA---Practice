class Solution:
    def divFloorCeil(self, a, b):
        Floor=a//b
        Ceil=-(-a//b)
        return [Floor,Ceil]
