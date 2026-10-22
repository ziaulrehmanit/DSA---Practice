import math

class Solution:
    def isPower(self, x: int, y: int) -> bool:
        # Edge cases based on mathematical rules
        if y <= 0: 
            return False  # Positive numbers raised to any real power remain positive
        if y == 1: 
            return True   # x^0 = 1 for any non-zero x
        if x <= 1: 
            return x == y # If x is 0 or 1, y must equal x to be a power
        
        # Calculate log base x of y
        res = math.log(y) / math.log(x)
        
        # Check if the result is an integer (accounting for floating-point precision)
        return math.isclose(res, round(res))
