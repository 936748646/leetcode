#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 设dp[i]: nums[i]到末尾的最长递增子序列长度
        # dp[i] = max(dp[i + 1], ..., dp[len(nums) - 1]) + 1
        # 其中，对应(nums[i + 1], ..., nums[len(nums) - 1])需要比nums[i]大
        dp = [0] * len(nums)
        dp[-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            max_res = 0
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    max_res = max(max_res, dp[j])
            dp[i] = max_res + 1
        # print(dp)
        return max(dp)
# @lc code=end

