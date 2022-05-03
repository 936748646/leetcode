#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        if l < 2:
            return s
        start = 0
        max_len = 0
        for i in range(l):
            if l - i - 1 < max_len // 2:
                break
            left = i
            right = i
            # 让right移动到没有重复的下一个字符（因为重复默认回文）
            while right + 1 < l and s[right + 1] == s[right]:
                right += 1
            i = right + 1  # 下次从重复的下一个字符开始判断
            while right + 1 < l and left > 0 and s[right + 1] == s[left - 1]:
                right += 1
                left -= 1
            if right - left + 1 > max_len:
                max_len = right - left + 1
                start = left
        return s[start: start + max_len]
# @lc code=end

