class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        seen = set()
        special = set()
        for i, num in enumerate(nums):
            if i == 0 or num != nums[i-1]:
                if num in seen:
                    special.discard(num)
                else:
                    seen.add(num)
                    special.add(num)
        return len(special)
