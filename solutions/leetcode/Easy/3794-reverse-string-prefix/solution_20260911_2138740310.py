class Solution:
    def reversePrefix(self, s: str, k: int) -> str:

        arr = list(s)
        i = 0
        while i < k:
            arr[i], arr[k-1] = arr[k-1], arr[i]
            i += 1
            k -= 1
        return ''.join(arr)
