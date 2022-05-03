#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [[0 for j in range(2)] for i in range(l)]
        dp[0][0] = 0
        dp[0][1] = nums[0]
        for i in range(1, l):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i]

        return max(dp[l - 1][0], dp[l - 1][1])
# @lc code=end

