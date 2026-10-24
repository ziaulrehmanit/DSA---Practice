class Solution:
    def maxLength(self, arr):
        
        prefix_map = {}
        max_length = prefix_sum = 0
        
        for i in range(len(arr)):
            
            prefix_sum += arr[i]
            
            if prefix_sum == 0:
                max_length = i + 1
                
            if prefix_sum in prefix_map:
                max_length = max(max_length, i - prefix_map[prefix_sum])
            else:
                prefix_map[prefix_sum] = i
                
        return max_length
