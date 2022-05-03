#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s) - 1, -1, -1):
            if res > 4 * dict[s[i]]:  # 例：IV——res=5时，发现res比I*4大，则需要减去I
                res -= dict[s[i]]
            else:
                res += dict[s[i]]
        return res
# @lc code=end

