#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    # 平方平方地算
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        res = 1
        m = abs(n)
        while m > 0:
            if m % 2 != 0:
                res *= x
            x *= x
            m //= 2
        if n >= 0:
            return res
        else:
            return 1/res
# @lc code=end

