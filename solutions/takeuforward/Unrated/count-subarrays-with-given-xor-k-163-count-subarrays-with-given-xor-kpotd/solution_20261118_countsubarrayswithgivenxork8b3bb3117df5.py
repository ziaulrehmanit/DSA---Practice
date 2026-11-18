class Solution:
    def subarraysWithXorK(self, nums, k):
        cnt = xor = 0
        freq = {0: 1}
        
        for num in nums:
            xor ^= num
            target = xor ^ k
            
            if target in freq:
                cnt += freq[target]
                
            freq[xor] = freq.get(xor, 0) + 1
            
        return cnt
