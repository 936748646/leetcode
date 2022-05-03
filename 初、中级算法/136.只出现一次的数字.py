#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 所有数字异或一遍就是结果
        # a^a = 0; a^0 = a; 异或满足交换律
        result = 0
        for n in nums:
            result ^= n
        return result

# @lc code=end

