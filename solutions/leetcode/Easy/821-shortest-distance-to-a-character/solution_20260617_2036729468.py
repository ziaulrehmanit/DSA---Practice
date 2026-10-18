class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        res = []
        for i in range(len(s)):

            if s[i] == c:
                res.append(0)
                continue

            distance1 = float('inf')
            distance2 = float('inf')

            d = 1
            j = i + 1
            while j < len(s):
                if s[j] == c:
                    distance1 = d
                    break
                d += 1
                j += 1
            
            d = 1
            k = i - 1
            while k >= 0:
                if s[k] == c:
                    distance2 = d
                    break
                d += 1
                k -= 1

            res.append(min(distance1, distance2))
        
        return res
