class Solution:
    def findFrequency(self, arr, x):
        freq = 0
        for num in arr:
            if num == x:
                freq += 1
        return freq
