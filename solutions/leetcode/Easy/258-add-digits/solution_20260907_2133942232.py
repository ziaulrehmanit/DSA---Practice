class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            x = num
            add = 0
            while x:
                add += (x % 10)
                x //= 10
            num = add
        return num
