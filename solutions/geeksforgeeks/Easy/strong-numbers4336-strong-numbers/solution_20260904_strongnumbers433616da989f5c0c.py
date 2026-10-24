class Solution:
    def isStrong(self, n):
        FACTORIALS = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

        # Store the original number to compare later
        original_number = n
        digit_sum = 0

        # Extract digits and sum their factorials
        while n > 0:
            digit = n % 10
            digit_sum += FACTORIALS[digit]
            n //= 10

        # Return True if the sum equals the original number, otherwise False
        return digit_sum == original_number
