from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = s1.split()
        words2 = s2.split()

        ans = []

        for word in words1:
            if words1.count(word) == 1 and words2.count(word) == 0:
                ans.append(word)

        for word in words2:
            if words2.count(word) == 1 and words1.count(word) == 0:
                ans.append(word)

        return ans
