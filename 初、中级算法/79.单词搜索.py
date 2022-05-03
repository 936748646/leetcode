#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if self.dfs(board, word, i, j, 0):
                    return True
        return False
    def dfs(self, board, word, i, j, index):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
            return False
        if index >= len(word) - 1:
            return True
        temp = board[i][j]
        board[i][j] = '0'
        res = self.dfs(board, word, i - 1, j, index + 1) or self.dfs(board, word, i + 1, j, index + 1) or self.dfs(board, word, i, j - 1, index + 1) or self.dfs(board, word, i, j + 1, index + 1)
        board[i][j] = temp
        return res
# @lc code=end

