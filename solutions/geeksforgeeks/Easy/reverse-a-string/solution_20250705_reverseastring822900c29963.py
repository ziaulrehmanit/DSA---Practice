#User function Template for python3

class Solution:
    def reverseString(self, s: str) -> str:
        # Convert string to list for in-place reversal
        to_list = list(s)
        
        # Initialize two pointers
        left, right = 0, len(to_list) - 1
        
        # Reverse the list in-place
        while left <= right:
            to_list[left], to_list[right] = to_list[right], to_list[left]
            left += 1
            right -= 1
        
        # Convert the list back to a string and return
        return ''.join(to_list)

             
        
        # Inbuilt String Method
