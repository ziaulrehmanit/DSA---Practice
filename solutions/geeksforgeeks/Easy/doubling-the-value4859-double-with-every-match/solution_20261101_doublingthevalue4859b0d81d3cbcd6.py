class Solution:
    def solve(self, b: int, arr: list[int]) -> int:
        for num in arr:
            if num == b:
                b *= 2
                
        return b
