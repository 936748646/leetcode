#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        return self.Fibonacci(n, 1, 1)
    def Fibonacci(self, n, a, b):
        if n <= 1:
            return b
        return self.Fibonacci(n - 1, b, a + b)
# @lc code=end

