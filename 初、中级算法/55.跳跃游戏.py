#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        min_step, flag, bool = 2, -1, True
        for i in range(len(nums) - 2, -1, -1):
            if flag == 0:
                if nums[i] >= min_step:
                    min_step = 2
                    flag = -1
                    bool = True
                else:
                    min_step += 1
            elif nums[i] == 0:
                flag = 0
                bool = False
        return bool
# @lc code=end

