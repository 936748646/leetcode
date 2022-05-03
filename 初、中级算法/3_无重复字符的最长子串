#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        dic = dict()
        max_len = 0
        j = 0
        for i in range(len(s)):
            if s[i] in dic.keys():
                j = max(j, dic[s[i]] + 1)
            dic[s[i]] = i
            max_len = max(max_len, i - j + 1)
        return max_len
# @lc code=end

