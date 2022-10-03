#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 0:
            return 0
        n = len(prices)
        dp0 = 0  # 卖出
        dp1 = -prices[0]  # 买入
        for i in range(1, n):
            dp0 = max(dp0, dp1 + prices[i])  # 当天不卖或卖
            dp1 = max(dp1, -prices[i])  # 当天不买或买
        return dp0  # 最后肯定是要卖出

# @lc code=end

