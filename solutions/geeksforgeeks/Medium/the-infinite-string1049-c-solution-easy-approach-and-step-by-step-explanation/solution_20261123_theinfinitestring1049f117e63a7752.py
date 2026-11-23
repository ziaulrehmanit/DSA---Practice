class Solution:
    def posInfinite(self, s: str, pos: int) -> str:
        lengths = [len(s)]
        step = 1
        
        while lengths[-1] < pos:
            lengths.append((2 * lengths[-1] + step))
            step += 1
            
        for i in range(len(lengths) - 1, 0, -1):
            prev_len = lengths[i - 1]
            curr_len = lengths[i]
            
            if prev_len >= pos:
                continue
            
            elif prev_len + i >= pos:
                return '$'
                
            else:
                pos = curr_len - pos + 1
                
        return s[pos - 1]
