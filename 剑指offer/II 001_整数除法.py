class Solution:
    def divide(self, a: int, b: int) -> int:
        # 让b不断扩大成2倍（b<<1），当b>a时记录b扩大的倍数和a的剩余大小
        # 再继续同样的方法看a剩余的能囊括多少b
        sign = -1 if (a > 0) ^ (b > 0) else 1
        a, b = abs(a), abs(b)
        res = 0
        while a >= b:
            n = 1
            val = b
            while a > (val << 1):
                n <<= 1  # 代表a大于多少个b（跟着val扩大两倍）
                val <<= 1
            a -= val  # a=a剩余的大小
            res += n
            # 至此如果a还>=b就再来一轮，以此类推...
        if sign == -1: res = -res
        return res if -2 ** 31 <= res <= 2 ** 31 - 1 else 2 ** 31 - 1  # 只有可能max越界，因为可能产生2147483648
