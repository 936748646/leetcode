#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0:
            return ""
        res = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(res) != 0:
                res = res[0: len(res) - 1]
            i += 1
        return res
# @lc code=end

