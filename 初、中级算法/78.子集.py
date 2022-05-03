#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []       
        path = []
        self.backTrack(res, nums, path, 0)
        return res
    def backTrack(self, res, nums, path, start):        
        temp = []
        for i in path:
            temp.append(i)
        res.append(temp)
        for i in range(start, len(nums)):
            path.append(nums[i])
            self.backTrack(res, nums, path, i + 1)
            del path[-1]
# @lc code=end

