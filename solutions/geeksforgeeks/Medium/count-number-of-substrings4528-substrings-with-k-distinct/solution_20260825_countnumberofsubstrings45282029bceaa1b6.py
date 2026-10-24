class Solution:
    def countAtMostK(self, string, x):
        count = 0
        left = 0
        freq = {}
        for right in range(len(string)):
            freq[string[right]] = freq.get(string[right], 0) + 1
            while len(freq) > x:
                freq[string[left]] -= 1
                if freq[string[left]] == 0:
                    del freq[string[left]]
                left += 1
            count += (right - left) + 1
        return count    
    def countSubstr (self, s, k):
        
        return self.countAtMostK(s, k) - self.countAtMostK(s, k-1)
