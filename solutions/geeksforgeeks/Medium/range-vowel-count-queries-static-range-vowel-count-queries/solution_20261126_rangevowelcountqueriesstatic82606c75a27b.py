class Solution:
    def countVowels(self, s: str, queries: list[list[int]]) -> list[int]:
        vowels = "aeiou"
        n = len(s)
        prefix = [0] * (n + 1)
        
        for index, char in enumerate(s):
            prefix[index+1] = prefix[index] + (1 if char in vowels else 0)
            
        return [prefix[r + 1] - prefix[l] for l, r in queries]
