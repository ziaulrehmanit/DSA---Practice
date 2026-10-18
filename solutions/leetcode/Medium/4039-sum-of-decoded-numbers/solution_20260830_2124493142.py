class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        modulo = 10 ** 9 + 7
        sum = 0
        for num in nums:
            width = num % 10
            d = num // 10
            s = str(num)
            x = int(s[:width])
            y = int(s[width:-1])
            sum = (sum + pow(x, y, modulo)) % modulo
        return sum
