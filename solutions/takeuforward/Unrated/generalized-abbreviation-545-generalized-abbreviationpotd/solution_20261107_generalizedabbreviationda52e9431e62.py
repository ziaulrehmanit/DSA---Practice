class Solution(object):
    def generateAbbreviations(self, word):
        res = []
        
        def backtrack(pos, cur, count):
            if pos == len(word):
                if count > 0:
                    cur += str(count)
                res.append(cur)
                return
            
            # Choice 1: Abbreviate the current character (increment count)
            backtrack(pos + 1, cur, count + 1)
            
            # Choice 2: Keep the current character
            # Append the accumulated count (if any) and the character itself
            next_cur = cur + (str(count) if count > 0 else "") + word[pos]
            backtrack(pos + 1, next_cur, 0)
            
        backtrack(0, "", 0)
        return res
