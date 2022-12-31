class Solution:
    def numSquares(self, n: int) -> int:
        # bfs：每个整数为节点，若两整数相差为一个完全平方数，则该两整数之间存在一条边
        # 即求n->0的最短路径
        queue = deque()
        visited = set()
        queue.append((n, 0))  # 记录节点和路径长度
        while queue:
            number, step = queue.popleft()
            targets = []  # 存放与number有边相连的节点
            for i in range(1, int(number ** 0.5) + 1):
                targets.append(number - i * i)
            for target in targets:
                if target == 0: return step + 1
                if target not in visited:
                    queue.append((target, step + 1))
                    visited.add(target)
        return 0
