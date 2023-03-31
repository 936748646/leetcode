class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix[0]) - 1
        # 从右上角的数开始，向左是小于它的，向下是大于它的
        while i < len(matrix) and j >= 0:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True
        return False
