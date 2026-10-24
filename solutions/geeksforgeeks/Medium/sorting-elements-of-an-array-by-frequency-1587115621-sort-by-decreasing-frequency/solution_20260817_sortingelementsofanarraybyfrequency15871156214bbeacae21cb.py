class Solution:
    def sortByFreq(self,s):
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        return sorted(arr, key = lambda x: (-freq[x], x))
