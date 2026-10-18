class Solution:
    def isPalindromic(self, s: str) -> bool:
        binary_array = [int(bit) for char in s for bit in format(ord(char), '08b')]
        return binary_array == binary_array[::-1]    
