class Solution:
	def longestSubarrayDivK(self, arr, k):
	    prefix_sum = longest = 0
	    HashMap = {0 : -1}
	    
	    for index, num in enumerate(arr):
	        prefix_sum += num
	        rem = prefix_sum % k
	        
	        if rem in HashMap:
	            longest = max(longest, index - HashMap[rem])
	        else:
	            HashMap[rem] = index
	            
	    return longest
