#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        res = []
        intervals.sort()
        temp = intervals[0]
        for i in range(1, len(intervals)):
            if temp[1] >= intervals[i][0]:
                temp = [min(temp[0],intervals[i][0]), max(temp[1], intervals[i][1])]
            else:
                res. append(temp)
                temp = intervals[i]
        res.append(temp)
        return res
# @lc code=end

