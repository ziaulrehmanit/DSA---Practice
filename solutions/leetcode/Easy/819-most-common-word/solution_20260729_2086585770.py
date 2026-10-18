import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        words = re.findall(r"[a-z]+", paragraph.lower())

        freq = {}
        ans = ""
        mx = 0

        for word in words:
            if word not in banned:
                freq[word] = freq.get(word, 0) + 1
                if freq[word] > mx:
                    mx = freq[word]
                    ans = word

        return ans
