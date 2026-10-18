class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        HashMap = {}

        for char in word:

            if char in HashMap:
                HashMap[char] += 1
            else:
                HashMap[char] = 1

        count = 0

        for char in HashMap:

            if char.isupper():
                continue

            if char.upper() in HashMap and HashMap[char.upper()] > 0:
                HashMap[char] -= 1
                HashMap[char.upper()] -= 1
                count += 1

        return count
