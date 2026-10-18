class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        ans = k
        while True:
            found = True
            for num in nums:
                if num == ans:
                    found = False
                    break
            if found:
                return ans
            ans += k
