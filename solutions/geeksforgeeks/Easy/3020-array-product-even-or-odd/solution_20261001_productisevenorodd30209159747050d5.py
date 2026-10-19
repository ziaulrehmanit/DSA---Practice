class Solution:
    def isProductEven(self, arr: list[int]) -> bool:
        
        for num in arr:
            if num % 2 == 0:
                return True
        return False
