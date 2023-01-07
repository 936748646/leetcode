class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 典型dfs问题，因为要把路走到底寻找可达性。
        # 节省时间：从边界出发反向遍历往高处找（这样就保证了都能流到边界）
        m, n = len(heights), len(heights[0])
        visited_pacific, visited_atlantic = set(), set()
        def dfs(x, y, visited):
            if (x, y) in visited: return
            visited.add((x, y))
            for (i, j) in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= i < m and 0 <= j < n and heights[i][j] >= heights[x][y]:
                    dfs(i, j, visited)
        # 太平洋的两条边
        for i in range(m):
            dfs(i, 0, visited_pacific)
        for j in range(n):
            dfs(0, j, visited_pacific)
        # 大西洋的两条边
        for i in range(m):
            dfs(i, n - 1, visited_atlantic)
        for j in range(n):
            dfs(m - 1, j, visited_atlantic)
        res = list(map(list, visited_pacific & visited_atlantic))  # 使用&求两个set交集（|为并集），使用map对set内的元素类型转换
        return res
