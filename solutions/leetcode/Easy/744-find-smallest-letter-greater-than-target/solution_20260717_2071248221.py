class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low, high = 0, len(letters)-1
        ans = letters[0]
        while low <= high:
            mid = (low + high) // 2
            if letters[mid] > target:
                high = mid - 1
                ans = letters[mid]
            else:
                low = mid + 1
        return ans if ans > target else letters[0]
