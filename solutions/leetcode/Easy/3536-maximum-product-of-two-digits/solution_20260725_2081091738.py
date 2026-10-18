class Solution:
    def maxProduct(self, n: int) -> int:
        max1 = max2 = -1
        while n > 0:
            mod = n % 10
            if mod > max1:
                max2 = max1
                max1 = mod
            elif mod > max2:
                max2 = mod
            n //= 10
        return max1*max2
