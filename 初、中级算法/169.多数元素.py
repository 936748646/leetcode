#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        count = 0
        for i in range(len(nums)):
            if res == nums[i]:
                count += 1
            else:
                count -= 1
                if count == 0:
                    res = nums[i + 1]
        return res
# @lc code=end

