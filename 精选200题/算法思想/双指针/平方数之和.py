class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i, j = 0, int(c ** 0.5)
        while i <= j:
            s = i * i + j * j
            if s == c: return True
            elif s < c: i += 1
            else: j -= 1
        return False
