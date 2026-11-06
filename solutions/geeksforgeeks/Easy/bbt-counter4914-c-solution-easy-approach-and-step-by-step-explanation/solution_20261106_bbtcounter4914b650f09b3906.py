class Solution:
    def countBT(self, h: int) -> int:
        if h == 0 or h == 1:
            return 1

        MOD = 10**9 + 7

        # dp_prev2 represents DP[i-2], initially DP[0] = 1
        # dp_prev1 represents DP[i-1], initially DP[1] = 1
        dp_prev2 = 1
        dp_prev1 = 1
        
        for i in range(2, h + 1):
            # Formula: DP[i] = DP[i-1] * (DP[i-1] + 2 * DP[i-2]) % MOD
            current = (dp_prev1 * (dp_prev1 + 2 * dp_prev2)) % MOD

            dp_prev2 = dp_prev1
            dp_prev1 = current

        return dp_prev1
