class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        # dp[i][j]=max(dp[i-1][j],dp[i][j-1])+grid[i][j]
        # 为节省空间，可以直接修改grid为dp
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0: continue
                if i == 0: grid[i][j] += grid[i][j - 1]
                elif j == 0: grid[i][j] += grid[i - 1][j]
                else: grid[i][j] += max(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]
