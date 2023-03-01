class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口，向右移动，把队列左边元素移出以满足题目要求，取最长的值
        if not s:
            return 0
        search = deque()
        max_len, cur_len = 0, 0
        for i in range(len(s)):
            cur_len += 1
            while s[i] in search:
                search.popleft()
                cur_len -= 1
            if cur_len > max_len: max_len = cur_len
            search.append(s[i])
        return max_len
