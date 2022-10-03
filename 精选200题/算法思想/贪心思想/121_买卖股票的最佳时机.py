class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 贪心：只要找到当前节点之前的最小价格买入，在当前价格卖出，看当前是否是最大收益
        # 动态规划方法见初中级算法
        min_price = prices[0]
        max_profix = 0
        for i in range(1, len(prices)):
            min_price = min(prices[i], min_price)
            max_profix = max(prices[i] - min_price, max_profix)
        return max_profix
