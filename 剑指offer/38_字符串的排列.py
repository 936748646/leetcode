class Solution:
    def permutation(self, s: str) -> List[str]:
        c, res = list(s), []
        def dfs(x):
            if x == len(c) - 1:  # x：当前固定位
                res.append(''.join(c))
                return
            dic = set()  # 保存已经交换到第x位过的字符
            for i in range(x, len(c)):  # 将第x位字符与第i位字符交换
                if c[i] in dic:  # 如果c[i]是已经交换过的重复的，则跳过
                    continue
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]  # 交换
                dfs(x + 1)
                c[i], c[x] = c[x], c[i]  # 换回来，换下一个c[i]
        dfs(0)
        return res
