class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 贪心：每当访问到一个prices[i]-prices[i-1]>0，就添加到收益中
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]: profit += (prices[i] - prices[i - 1])
        return profit
