class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = []       
        return self.dfs(visited, m, n, k, 0, 0, 0, 0)
    # dfs向下和向右搜索
    def dfs(self, visited, m, n, k, i, j, si, sj):
        if i >= m or j >= n or si + sj > k or [i, j] in visited:
            return 0
        visited.append([i, j])
        # 数位和增量公式：
        # s_x + 1 if (x + 1) % 10 else s_x - 8
        return 1 + self.dfs(visited, m, n, k, i + 1, j, si - 8 if (i + 1) % 10 == 0 else si + 1, sj) + self.dfs(visited, m, n, k, i, j + 1, si, sj - 8 if (j + 1) % 10 == 0 else sj + 1)
