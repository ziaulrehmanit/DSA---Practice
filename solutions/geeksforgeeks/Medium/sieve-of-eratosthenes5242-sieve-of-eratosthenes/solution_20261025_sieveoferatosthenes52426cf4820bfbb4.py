class Solution:
    def sieve(self, n):

        if n < 2:
            return []

        arr = [1] * (n + 1)
        arr[0] = arr[1] = 0

        for i in range(2, int(n ** 0.5) + 1):
            if arr[i]:
                for j in range(i * i, n+1, i):
                    arr[j] = 0

        return [i for i in range(2, n+1) if arr[i]]
