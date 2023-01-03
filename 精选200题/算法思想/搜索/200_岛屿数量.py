class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count, row, col = 0, len(grid), len(grid[0])
        def dfs(x, y):  # 遍历岛屿，每次该函数结束，就是已经遍历完一个岛屿，count可以加一
            if not (0 <= x < row and 0 <= y < col) or grid[x][y] == "0": return
            grid[x][y] = "0"
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count
