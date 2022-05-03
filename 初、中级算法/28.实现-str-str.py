#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        right = len(needle)
        if right == 0:
            return 0
        while right <= len(haystack):
            if haystack[left: right] == needle:
                return left
            left += 1
            right += 1
        return -1

# @lc code=end

