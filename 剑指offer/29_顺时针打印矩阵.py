class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        i, j, li, lj, res = 0, 0, len(matrix) - 1, len(matrix[0]) - 1, []
        next = 0  # 下一步方向。0: 右; 1: 下; 2: 左; 3: 上
        # 将打印过的赋值为''
        while matrix[i][j] != '':
            res.append(matrix[i][j])
            matrix[i][j] = ''
            if next == 0:
                if j != lj and matrix[i][j + 1] != '':
                    j += 1
                else:
                    next = 1
                    i += 1
            elif next == 1:
                if i != li and matrix[i + 1][j] != '':
                    i += 1
                else:
                    next = 2
                    j -= 1
            elif next == 2:
                if j != 0 and matrix[i][j - 1] != '':
                    j -= 1
                else:
                    next = 3
                    i -= 1
            elif next == 3:
                if i != 0 and matrix[i - 1][j] != '':
                    i -= 1
                else:
                    next = 0
                    j += 1
            if i > li or j > lj or i < 0 or j < 0:
                break
        return res
