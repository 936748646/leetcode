class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for i in range(0, len(nums))]  # dp[i]：以nums[i]结尾的连续子数组最大和
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i] + max(0, dp[i - 1])
        return max(dp)
