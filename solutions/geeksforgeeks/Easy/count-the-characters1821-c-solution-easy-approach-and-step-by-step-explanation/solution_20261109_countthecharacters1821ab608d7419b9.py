from collections import Counter

class Solution:
    def getCount (self, s, k):
        
        groups = Counter()
        
        prev = None
        for char in s:
            if char != prev:
                groups[char] += 1
                prev = char
                
        return sum(1 for count in groups.values() if count == k)
