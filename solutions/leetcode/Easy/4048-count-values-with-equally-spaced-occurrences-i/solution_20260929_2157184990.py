from collections import Counter
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        freq = Counter(nums)
        n = len(nums)
        cnt = 0
        for num in freq:
            if freq[num] == 3:
                ind1 = ind2 = ind3 = None
                for i in range(n):
                    if nums[i] == num:
                        if ind1 == None:
                            ind1 = i
                        elif ind2 == None:
                            ind2 = i
                        else:
                            ind3 = i
                            break
                if ind2 - ind1 == ind3 - ind2:
                    cnt += 1
        return cnt
