class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        count = 0

        for i in range(len(s)-1, -1, -1):

            if s[i] == ' ' and i != len(s)-1 and s[i+1] != ' ':
                break
            elif s[i] != ' ':
                count += 1
                
        return count
