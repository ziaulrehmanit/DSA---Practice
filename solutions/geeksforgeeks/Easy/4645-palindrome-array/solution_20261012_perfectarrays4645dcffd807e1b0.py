class Solution:
    def isPalindrome(self, arr):
        i, j = 0, len(arr)-1
        while i < j:
            if arr[i] != arr[j]:
                return False
            i += 1
            j -= 1
        return True
