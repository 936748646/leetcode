class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        # dp[i][j]：i个骰子点数和j的概率，可向后推出dp[i+1][j+1]、dp[i+1][j+2]...dp[i+1][j+6]
        # 只使用两个一维数组dp、tmp交替前进
        dp = [1 / 6] * 6  # 1个骰子的点数和概率
        for i in range(2, n + 1):  # 从2个骰子开始
            tmp = [0] * (5 * i + 1)  # i个骰子点数和范围[i,6i]，因此一共有6i-i+1=5i+1种可能
            for j in range(len(dp)):
                for k in range(6):
                    tmp[j + k] += dp[j] / 6  # 加上之前算出的i-1个骰子相应的点数和概率乘1/6，1/6指第i个骰子投出k的概率
            dp = tmp
        return dp
