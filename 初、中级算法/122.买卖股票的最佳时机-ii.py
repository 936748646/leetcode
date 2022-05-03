#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
import re
from typing import List


class Solution:
    '''
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for j in range(2)] for i in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])
        
        return dp[n - 1][0]
    '''
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp0 = 0
        dp1 = -prices[0]
        for i in range(1,n):
            newDp0 = max(dp0, dp1 + prices[i])
            newDp1 = max(dp0 - prices[i], dp1)
            dp0 = newDp0
            dp1 = newDp1
        
        return dp0
# @lc code=end

