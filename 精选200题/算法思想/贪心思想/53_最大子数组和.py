class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        preSum, maxSum = nums[0], nums[0]
        for i in range(1, len(nums)):
            if preSum > 0: preSum += nums[i]  # 如果前面的和大于0，就加上目前的nums[i]，再和维护的maxSum比较，保留大的
            else: preSum = nums[i]
            maxSum = max(preSum, maxSum)
        return maxSum
