class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        
        res = []
        for word in words:
            charSum = 0
            for i in range(len(word)):
                charSum += weights[ord(word[i])-97]
            char = charSum%26
            res.append(chr(122-char))
        return ''.join(res)
