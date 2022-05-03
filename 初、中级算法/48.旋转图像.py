#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        for i in range(0, l // 2):
            for j in range(i, l - i - 1):
                temp = matrix[i][j]
                m = l - j - 1
                n = l - i - 1
                matrix[i][j] = matrix[m][i]
                matrix[m][i] = matrix[n][m]
                matrix[n][m] = matrix[j][n]
                matrix[j][n] = temp
# @lc code=end

