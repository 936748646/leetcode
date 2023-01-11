class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 每一小段为一个节点，每段截取1/2/3个数字，因此每个节点只能有三个分支
        # 根据①截取后剩余元素个数是否合理；②截取的小段格式是否正确（<=255，无前导0）剪枝

        length = len(s)
        if length < 4 or length > 12: return []

        def dfs(length, seg, begin, path, res):
            if len(path) == length + 4:  # 最后一个path后面还有个点，去掉
                res.append(path[:-1])
                return
            for i in [1, 2, 3]:  # 每小段截取1/2/3个数字
                check1 = (0 <= length - begin - i <= 3 * (4 - seg - 1))  # 截取i个数字后剩余的元素个数合理（4-seg-1为剩余段数，剩下的数字只能被分为这么多段）
                if begin < length:  # 可能begin+i>length
                    check2 = (int(s[begin: begin + i]) <= 255)  # 每个小段的数字要小于等于255
                    check3 = False if i > 1 and s[begin] == "0" else True  # 每个小段不能含有前导0
                else:
                    check2, check3 = False, False
                if check1 and check2 and check3:
                    path += s[begin: begin + i] + "."
                    dfs(length, seg + 1, begin + i, path, res)
                    path = path[:-(i + 1)]  # 回溯复原（+1是末尾的点）
        
        seg = 0  # 当前截到第几段
        begin = 0  # 当前从第几个数字开始处理
        path = ""  # 当前状态
        res = []
        dfs(length, seg, begin, path, res)
        return res
