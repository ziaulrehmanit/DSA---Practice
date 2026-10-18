class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        n = len(words)
        arr = []
        for i in range(n):
            if x in words[i]:
                arr.append(i)
        return arr
