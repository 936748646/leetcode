class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 到达岛屿第一个点后，分别向东南西北四个方向前进，若为水或已访问的岛屿点则停止前进；
        # 到达新的岛屿点后继续以该点向东南西北四个方向前进，以此类推
        res, row, col = 0, len(grid), len(grid[0])
        def dfs(x, y):  # 计算岛屿面积：递归，返回步长
            if not (0 <= x < row and 0 <= y < col): return 0
            if grid[x][y] == 1:
                grid[x][y] = 0
                return 1 + dfs(x - 1, y) + dfs(x + 1, y) + dfs(x, y - 1) + dfs(x, y + 1)
            return 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1: res = max(dfs(i, j), res)
        return res
