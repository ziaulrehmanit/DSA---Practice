class Solution:
    def subsequenceSum(self, s):
        MOD = 10**9 + 7
        power = pow(2, len(s) - 1, MOD)
        digits_sum = sum(int(char) for char in s)
        return (digits_sum * power) % MOD
