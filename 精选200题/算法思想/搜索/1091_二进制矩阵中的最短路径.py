class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        l = len(grid)
        if grid[0][0] != 0 or grid[l - 1][l - 1] != 0: return -1
        direction = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        queue = [(0, 0, 1)]  # 记录位置和长度计数
        grid[0][0] = 1
        for i, j, cnt in queue:
            if i == l - 1 and j == l - 1: return cnt
            for dx, dy in direction:
                x, y = i + dx, j + dy
                if 0 <= x < l and 0 <= y < l and grid[x][y] == 0:
                    grid[x][y] = 1  # 已走过的标记为1
                    queue.append((x, y, cnt + 1))  # bfs，把所有下一个direction中可达的节点放入队列
        return -1
