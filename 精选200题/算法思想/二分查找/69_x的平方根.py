class Solution:
    def mySqrt(self, x: int) -> int:
        # 二分法
        if x <= 1: return x
        l, r = 1, x
        while l <= r:
            m = l + (r - l) // 2
            if m * m == x: return m
            if m * m > x: r = m - 1
            else: l = m + 1
        return r
