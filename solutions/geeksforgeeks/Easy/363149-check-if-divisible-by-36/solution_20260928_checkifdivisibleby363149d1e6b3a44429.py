class Solution:
    def checkDivisibleBy36(self, s):
        
        # Base cases for single-digit inputs
        if len(s) == 1:
            return s == '0'
            
        # 1. Check divisibility by 4 (last two digits)
        if int(s[-2:]) % 4 != 0:
            return False
            
        # 2. Check divisibility by 9 (sum of all digits)
        d_sum = sum(int(ch) for ch in s)
        
        return d_sum % 9 == 0
