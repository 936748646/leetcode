class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(p), len(s)
        if n < m:
            return []
        res = []
        count_p, count_s = [0] * 26, [0] * 26
        for i in range(m):  # 先初始化一个滑动窗口count_s
            count_p[ord(p[i]) - ord('a')] += 1
            count_s[ord(s[i]) - ord('a')] += 1
        if count_p == count_s:
            res.append(0)
        for i in range(m, n):  # i为滑动窗口右侧新增的一格，i每增加一格，滑动窗口左侧就去除一格
            count_s[ord(s[i - m]) - ord('a')] -= 1  # 左侧去除一格
            count_s[ord(s[i]) - ord('a')] += 1
            if count_s == count_p:
                res.append(i - m + 1)
        return res
