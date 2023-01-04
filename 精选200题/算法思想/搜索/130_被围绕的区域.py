class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # bfs遍历寻找以每个边界0起点的相连的0，标记为A
        # 最后再把标记的保持0，未标记的转为X
        m, n = len(board), len(board[0])
        def dfs(x, y):
            if not 0 <= x < m or not 0 <= y < n or board[x][y] != "O": return
            board[x][y] = "A"
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
        # 从每个边界开始找O
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "A": board[i][j] = "O"
                elif board[i][j] == "O": board[i][j] = "X"
