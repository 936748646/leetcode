#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#

# @lc code=start
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if k != 0:
            k %= l
            nums.reverse()
            nums[0: k] = list(reversed(nums[0: k]))
            nums[k:] = list(reversed(nums[k:]))

# @lc code=end

