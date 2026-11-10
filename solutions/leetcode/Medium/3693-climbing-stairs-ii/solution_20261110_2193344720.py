class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        if n == 0:
            return 0
            
        dp = [0] * (n + 1)
        
        for j in range(1, n + 1):
            step_cost = costs[j - 1]
            
            option1 = dp[j - 1] + step_cost + 1            # (j - (j-1))^2 = 1
            option2 = dp[j - 2] + step_cost + 4 if j >= 2 else float('inf')  # (j - (j-2))^2 = 4
            option3 = dp[j - 3] + step_cost + 9 if j >= 3 else float('inf')  # (j - (j-3))^2 = 9
            
            dp[j] = min(option1, option2, option3)
            
        return dp[n]
