class Solution:
    def mirrorDistance(self, n: int) -> int:
        
        reverse = 0
        duplicate = n

        while duplicate > 0:

            reverse = (reverse * 10) + (duplicate % 10)
            duplicate //= 10

        return abs(n - reverse)
