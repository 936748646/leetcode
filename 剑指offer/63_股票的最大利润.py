class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i]=max(dp[i-1],prices[i]-min(prices[0:i]))
        # 为了降低min(prices[0:i])遍历prices的时间复杂度：用一个变量cost每日更新记录最低价
        # 只用一个变量代替dp列表
        cost, dp = float("inf"), 0  # Python中可这样表示正负无穷：float("inf")，float("-inf")
        for price in prices:
            cost = min(cost, price)
            dp = max(dp, price - cost)
        return dp
