from collections import Counter
class Solution:
    def isGood(self, nums: List[int]) -> bool:

        maxi = max(nums)
        n = len(nums)

        if n != maxi+1:
            return False

        freq = Counter(nums)

        if freq[maxi] != 2:
            return False

        for i in range(1, maxi):
            if freq[i] != 1:
                return False

        return True
