#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        self.backTrack(nums, res, path)
        return res
    def backTrack(self, nums, res, path):
        if len(path) >= len(nums):
            temp = []
            for i in path:
                temp.append(i)
            res.append(temp)
            return
        for i in range(0, len(nums)):
            if nums[i] in path:
                continue
            path.append(nums[i])
            self.backTrack(nums, res, path)
            del path[-1]
# @lc code=end

