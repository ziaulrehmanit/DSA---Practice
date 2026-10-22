class Solution:
    def sandwichedVowel(self, s):
        
        def isVowel(char):
            return char in "aeiou"

        arr = list(s)

        for i in range(1, len(arr) - 1):
            if isVowel(arr[i]) and not isVowel(arr[i - 1]) and not isVowel(arr[i + 1]):
                arr[i] = ""

        return "".join(arr)
