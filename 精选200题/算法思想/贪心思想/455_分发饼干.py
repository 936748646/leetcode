class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 先满足满足度小的孩子，把尽量小的饼干分配给孩子
        g.sort()
        s.sort()
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                j += 1
            else: j += 1
        return i 
