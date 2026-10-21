class Solution:
    def longestSubarray(self, arr):
        
        max_length = length = 0
        
        for num in arr:
            
            if num < 0:
                length = 0
            else:
                length += 1
                
            max_length = max(max_length, length)
            
        return max_length
