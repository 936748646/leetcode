#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = [0 for i in range(26)]
        l = len(s)
        for i in range(l):
            count[ord(s[i]) - ord('a')] += 1
        for i in range(l):
            if count[ord(s[i]) - ord('a')] == 1:
                return i
        return -1
# @lc code=end

