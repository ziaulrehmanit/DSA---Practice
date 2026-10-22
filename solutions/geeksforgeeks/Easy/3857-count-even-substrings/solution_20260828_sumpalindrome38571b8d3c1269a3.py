class Solution:
    def isSumPalindrome (self, n):
        # We can run up to 5 additions (6 checks total)
        for i in range(6):
            # 1. Check if the current number is a palindrome
            if str(n) == str(n)[::-1]:
                return n

            # 2. If it's not a palindrome after 5 additions, stop and return -1
            if i == 5:
                return -1

            # 3. Otherwise, add the number to its reverse
            n = n + int(str(n)[::-1])

            # 4. Handle the platform's 32-bit overflow bug if needed
            if n > 2147483647:
                return -1

        return -1
