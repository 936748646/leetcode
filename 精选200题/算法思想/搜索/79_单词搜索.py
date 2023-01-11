class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 典型回溯：外层遍历先找到word第一个字母相同的元素，进入递归（访问过的要标记）
        # 内层递归dfs，如果匹配不到就返回False
        if not board: return False
        def backtrack(x, y, word, mark):
            if len(word) == 0: return True
            for d in directions:
                cur_x = x + d[0]
                cur_y = y + d[1]
                if 0 <= cur_x < len(board) and 0 <= cur_y < len(board[0]) and board[cur_x][cur_y] == word[0]: 
                    if mark[cur_x][cur_y] == 1: continue
                    mark[cur_x][cur_y] = 1  # 标记使用该元素
                    if backtrack(cur_x, cur_y, word[1:], mark): return True  # 往下搜索，如果匹配上了就返回True
                    else: mark[cur_x][cur_y] = 0  # 没匹配成功就回溯
            return False
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        mark = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    mark[i][j] = 1
                    if backtrack(i, j, word[1:], mark): return True
                    else: mark[i][j] = 0  # 回溯
        return False
