class Solution:
    def cntSubarrays(self, arr, k):
        
        HashMap = {0 : 1}
        count = 0
        current_sum = 0
        
        for num in arr:
            current_sum += num
            count += HashMap.get(current_sum - k, 0)
            HashMap[current_sum] = HashMap.get(current_sum, 0) + 1
            
        return count
