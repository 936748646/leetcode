class Solution:
    # 递归，本来应该在n=1时停止递归，但不能用判断语句
    def __init__(self):
        self.res = 0
    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)  # 短路效应：and或or会在第一条件不符或符合后跳过执行第二条件
        self.res += n
        return self.res
