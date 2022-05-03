#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        minval = -2**31
        maxval = 2**31 - 1
        if dividend == 0:
            return 0
        elif dividend == minval and divisor == -1:
            return maxval
        elif dividend == minval and divisor == minval:
            return 1
        elif divisor == minval:
            return 0
        res = 0
        flag = dividend ^ divisor
        if dividend == minval:
            dividend += abs(divisor)
            res += 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        for i in range(31, -1, -1):
            if (dividend >> i) >= divisor:
                res += (1 << i)
                dividend -= (divisor << i)
        return res if flag >= 0 else -res
        
# @lc code=end

