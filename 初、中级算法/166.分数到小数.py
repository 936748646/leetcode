#
# @lc app=leetcode.cn id=166 lang=python3
#
# [166] 分数到小数
#

# @lc code=start
class Solution:
    # 找循环节：看是否出现余数循环
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        if denominator == 0:
            return ""
        res = ""
        if (numerator ^ denominator) < 0:
            res += "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        res += str(numerator // denominator)
        remainder = numerator % denominator
        if remainder == 0:
            return res
        res += "."
        remainder_map = {}
        while remainder and remainder not in remainder_map:
            remainder_map[remainder] = len(res)
            remainder *= 10
            res += str(remainder // denominator)
            remainder %= denominator
        if remainder:
            res = res[:remainder_map[remainder]] + "(" + res[remainder_map[remainder]:]
            res += ")"
        return res
# @lc code=end

