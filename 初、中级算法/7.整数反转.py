#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        x_temp = abs(x)  # python负数存储方式不同，负数运算会出错
        max_int = (2**31 - 1) // 10
        while x_temp != 0:
            t = x_temp % 10
            if res > max_int:
                return 0
            res = res * 10 + t
            x_temp //= 10
        if x < 0:
            res = -res
        return res

# @lc code=end

