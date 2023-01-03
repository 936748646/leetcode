class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # 城市为节点，dfs找到城市连通图中连通域的个数（即连通分量）
        provinces, cities = 0, len(isConnected)
        visited = set()
        def dfs(i):  # dfs查找和城市i相连的
            for j in range(cities):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)
        for i in range(cities):
            if i not in visited:
                dfs(i)
                provinces += 1
        return provinces
