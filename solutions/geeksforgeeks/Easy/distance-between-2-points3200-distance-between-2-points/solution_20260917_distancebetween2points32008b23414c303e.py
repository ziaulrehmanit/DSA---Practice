class Solution:
    def distance(self, x1: int, y1: int, x2: int, y2: int) -> int:
        
        return round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)
