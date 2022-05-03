#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 0:
                self.swap(nums, i, left)
                left += 1
            elif nums[i] == 2:
                self.swap(nums, i, right)
                right -= 1
                i -= 1  # 还要重新判断交换过来的nums[right]
            i += 1

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
# @lc code=end

