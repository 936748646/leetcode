class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = min(dp[i-coin[0]],dp[i-coin[1]]...,dp[i-coin[j]])+1
        dp = [0] * (amount + 1)
        for i in range(1, amount + 1):
            min_val = float('inf')
            for c in coins:
                if i - c >= 0:
                    min_val = min(min_val, dp[i - c] + 1)
            dp[i] = min_val
        if dp[amount] != float('inf'):
            return dp[amount]
        return -1
        
