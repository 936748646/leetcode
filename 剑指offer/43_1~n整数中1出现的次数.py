class Solution:
    # 设置cur为当前位，high为高位，low为低位
    # 计算每一位出现1的次数的总和
    # 方法：固定该位，看不大于n的情况下其他位有多少种情况
    def countDigitOne(self, n: int) -> int:
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:  # high和cur同时为0时，已越过最高位，停止计算
            # cur有0、1、2~9三种情况
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += (high + 1) * digit
            low += cur * digit  # 将cur加入low，组成下轮low
            cur = high % 10
            high //= 10
            digit *= 10
        return res
