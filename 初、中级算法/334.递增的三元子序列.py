#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#

# @lc code=start
import sys


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = sys.maxsize
        mid = sys.maxsize
        for i in nums:
            if i < small:
                small = i
            elif i > small and i < mid:
                mid = i
            elif i > mid:
                return True
        return False
# @lc code=end

