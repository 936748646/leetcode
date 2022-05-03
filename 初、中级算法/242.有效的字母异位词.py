#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0 for i in range(26)]
        for letter in s:
            count[ord(letter) - ord('a')] += 1
        for letter in t:
            count[ord(letter) - ord('a')] -= 1
        for c in count:
            if c != 0:
                return False
        return True
# @lc code=end

