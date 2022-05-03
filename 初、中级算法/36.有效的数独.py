#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        l = len(board)
        line = [[0 for i in range(l)] for j in range(l)]
        column = [[0 for i in range(l)] for j in range(l)]
        cell = [[0 for i in range(l)] for j in range(l)]
        for i in range(l):
            for j in range(l):
                if board[i][j] == ".":
                    continue
                num = int(board[i][j]) - 1
                k = i // 3 * 3 + j // 3
                if line[i][num] != 0 or column[j][num] != 0 or cell[k][num] != 0:
                    return False
                line[i][num] = column[j][num] = cell[k][num] = 1
        return True

# @lc code=end

