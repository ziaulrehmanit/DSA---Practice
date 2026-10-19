class Solution:
    def gcd(self, n, arr):
        def check(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        ans = arr[0]
        for i in range(1, n):
            ans = check(ans, arr[i])
        return ans
