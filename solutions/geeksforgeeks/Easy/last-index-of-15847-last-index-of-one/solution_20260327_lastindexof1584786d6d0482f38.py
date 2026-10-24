class Solution:
    def lastIndex(self, s: str) -> int:
        
        indexOf1 = -1
        
        for i in range(len(s)-1,-1,-1):
            
            if s[i]=='1':
                indexOf1 = i
                break
        
        return indexOf1
