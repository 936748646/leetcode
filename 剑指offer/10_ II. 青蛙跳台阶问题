class Solution:
    # 斐波那契数列
    def numWays(self, n: int) -> int:
        if n <= 1:
            return 1
        dp = [1, 1]
        for i in range(2, n + 1):
            dp.append((dp[i - 1] + dp[i - 2]) % 1000000007)
        return dp.pop()
