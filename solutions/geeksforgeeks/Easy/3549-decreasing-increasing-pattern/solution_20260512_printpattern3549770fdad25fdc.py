class Solution:
    def pattern(self, N):
        res = []

        def solve(x):
            res.append(x)

            # Base condition
            if x <= 0:
                return

            solve(x - 5)

            # Add again while backtracking
            res.append(x)

        solve(N)
        return res
