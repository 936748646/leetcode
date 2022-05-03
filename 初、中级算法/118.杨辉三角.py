#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[] for i in range(0, numRows)]
        res[0].append(1)
        for i in range(1, numRows):
            res[i].append(1)
            for j in range(1, i):
                res[i].append(res[i - 1][j - 1] + res[i - 1][j])
            res[i].append(1)
        return res
# @lc code=end

