class Solution:
    def freqSorted(self, arr):
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        for num in sorted(freq):
            print(num, freq[num], end = '\n')
