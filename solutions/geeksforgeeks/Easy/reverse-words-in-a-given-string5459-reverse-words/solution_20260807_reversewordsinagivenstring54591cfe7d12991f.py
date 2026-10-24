class Solution:
    def reverseWords(self, s: str) -> str:
        arr = [word for word in s.split(".") if word]
        left, right = 0, len(arr)-1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return ".".join(arr)
