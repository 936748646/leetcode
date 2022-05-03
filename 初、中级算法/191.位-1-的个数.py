#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        # return bin(n).count('1')
        res = 0
        while n:
            res += (n & 1)  # 比较1与n的最后一位，相同为1，不同为0
            n >>= 1
        return res
# @lc code=end

