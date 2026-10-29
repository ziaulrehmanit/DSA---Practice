class Solution(object):
    def boldWords(self, words, s):
        n = len(s)
        # Array to mark if the character at index i should be bolded
        is_bold = [False] * n
        
        for word in words:
            word_len = len(word)
            start = s.find(word)
            while start != -1:
                # Mark all characters within this matching word interval as True
                for i in range(start, start + word_len):
                    is_bold[i] = True
                # Move 1 index forward to catch overlapping matches (e.g., "aba" in "ababa")
                start = s.find(word, start + 1)
                
        result = []
        i = 0
        while i < n:
            if is_bold[i]:
                result.append("<b>")
                while i < n and is_bold[i]:
                    result.append(s[i])
                    i += 1
                result.append("</b>")
            else:
                result.append(s[i])
                i += 1
                
        return "".join(result)
