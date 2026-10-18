class Solution:
    def checkGoodInteger(self, n: int) -> bool:

        digitSum = squareSum = 0

        while n > 0:
            digit = n%10
            digitSum += digit
            squareSum += digit * digit
            n = n // 10

        return True if squareSum - digitSum >= 50 else False
