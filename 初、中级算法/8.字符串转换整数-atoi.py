#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start


class Solution:
    def myAtoi(self, s: str) -> int:
        l = len(s)
        index = 0
        res = 0
        while index < l and s[index] == ' ':
            index += 1
        if index >= l:
            return 0
        sign = 1
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1
        INTEGER = 2**31
        while index < l:
            if not s[index].isdigit():
                break
            num = ord(s[index]) - ord('0')
            res = res * 10 + num
            if res > INTEGER - 1 and sign > 0:
                return INTEGER - 1
            elif res > INTEGER and sign < 0:
                return INTEGER * sign
            index += 1
        return res * sign

# @lc code=end

