class Solution:
    def kthDigit(self, a: int, b: int, k: int) -> int:
        # Python ints have arbitrary precision, so a ** b is exact.
        # Worst case 15 ** 15 ~ 4.4e17 (fits even in a signed 64-bit int
        # in other languages, so this approach ports cleanly).
        power = a ** b

        # Shift right by (k - 1) decimal places so the kth digit from the
        # right becomes the units digit.
        # Example: power = 27, k = 2 -> 27 // 10 = 2.
        shifted = power // (10 ** (k - 1))

        # The units digit of the shifted number is the answer.
        return shifted % 10
