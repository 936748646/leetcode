#
# @lc app=leetcode.cn id=738 lang=python3
#
# [738] 单调递增的数字
#

# @lc code=start
# 从后往前遍历，如果前一位的值大于后一位的值就把前位减一然后把后位变9

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n < 10:
            return n
        res = list(str(n))  # list()只能转str
        res[-1] = int(res[-1])
        for i in range(len(res) - 2, -1, -1):
            res[i] = int(res[i])
            if res[i] > res[i + 1]:
                res[i] = res[i] - 1
                for j in range(i + 1, len(res)):
                    res[j] = 9
        res = [str(x) for x in res]  # join()只能转str
        return int(''.join(res))  # int()只能转str
        # 以上两句也可直接用：
        # return int(''.join(map(str, res)))
# @lc code=end

