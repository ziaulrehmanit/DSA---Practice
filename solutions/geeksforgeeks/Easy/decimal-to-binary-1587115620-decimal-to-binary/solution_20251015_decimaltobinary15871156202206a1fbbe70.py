class Solution:
    def decToBinary(self, n):
        binary=str(bin(n))
        return binary[2:]
