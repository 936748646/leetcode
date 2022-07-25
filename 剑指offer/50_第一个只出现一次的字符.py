class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic  # 第一次出现就是true，之后再出现就都是false
        for k, v in dic.items():
            if v: return k
        return ' '
