#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel 表列序号
#

# @lc code=start

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        d = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,
        'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,
        'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,
        'V':22,'W':23,'X':24,'Y':25,'Z':26}
        k = len(columnTitle) - 1
        res = 0
        for c in columnTitle:
            res += d[c] * (26 ** k)
            k -= 1
        return res
# @lc code=end

