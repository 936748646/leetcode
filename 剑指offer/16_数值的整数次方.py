class Solution:
    # n转为二进制b_m...b_1，则x^n就等于将所有x^(b_i*2^(i-1))乘起来
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        res = 1
        if n < 0:
            x, n = 1 / x, -n
        while n:
            if n & 1 == 1:
                res *= x
            x *= x  # 每右移一位x就平方一下
            n >>= 1
        return res
