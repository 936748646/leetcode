class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # dict存储每个字符出现的最后位置，窗口移动时更新滑动窗口左边界。
        h = dict()  # 存储字符最后一次出现的位置
        left = -1
        res = 0
        for right in range(len(s)):
            if s[right] in h:
                left = max(h[s[right]], left)
            h[s[right]] = right
            res = max(res, right - left)
        return res
