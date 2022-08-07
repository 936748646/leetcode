class Solution:
    def strToInt(self, str: str) -> int:
        # 难点在于判断是否越界：下轮res=10*此轮res+当前数字x
        # 判断此轮res是否>2147483647//10=214748364
        # 如果大于，则肯定越界；如果等于，则x>7会越界，x<=7不会
        str = str.strip()
        if not str: return 0
        int_max, int_min, boundary = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10
        res, i, sign = 0, 0, 1  # i：开始拼接的索引位置
        if str[0] == '-': i, sign = 1, -1
        elif str[0] == '+': i = 1
        for c in str[i:]:
            if not '0' <= c <= '9': break
            if res > boundary or res == boundary and c > '7':
                return int_max if sign == 1 else int_min
            res = 10 * res + ord(c) - ord('0')
        return sign * res
