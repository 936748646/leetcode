class Solution:
    def cuttingRope(self, n: int) -> int:
        # dp[i]表示长度为i的绳子的最大乘积
        dp = [0 for i in range(n + 1)]
        dp[2] = 1
        for i in range(3, n + 1):  # 绳长
            for j in range(2, i):  # 剪第一段的长度
                # 3种情况：
                # 1. 不剪（dp[i]）
                # 2. 只剪第一段（j*(i-j)）
                # 3. 剪第一段，剩下也剪（j*dp[i-j]）
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
        return dp[n]
