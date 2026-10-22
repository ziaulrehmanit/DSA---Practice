class Solution:
    def reverseWords(self, s: str) -> str:
        arr = [word for word in s.split() if word]
        for i in range(len(arr)):
            arr[i] = arr[i][::-1]
        return ' '.join(arr)
