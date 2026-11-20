class Solution:
    def minFlips(self, s):
        
        flips_of_first_bit_0 = 0
        
        for ind, char in enumerate(s):
            if (ind%2 == 1 and char == '0') or (ind%2 == 0 and char == '1'):
                flips_of_first_bit_0 += 1
                
        return min(flips_of_first_bit_0, len(s) - flips_of_first_bit_0)
