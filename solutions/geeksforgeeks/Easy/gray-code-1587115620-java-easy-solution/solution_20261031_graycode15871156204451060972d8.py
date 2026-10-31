class Solution:
    def binaryToGray(self, n):
        # >> operation: 
        # The rightmost bit falls off, and single 0 is added to the leftmost position.
        # ^ operation: Outputs 1 if the bits are different, 0 if the bits are the same.
        return n ^ (n >> 1)
