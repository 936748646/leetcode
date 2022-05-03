#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3 的幂
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and (n == 1 or (n % 3 == 0 and self.isPowerOfThree(n / 3)))
# @lc code=end

