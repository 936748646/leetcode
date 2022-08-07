class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def recur(i, j):
            if i >= j:
                return True
            p = i
            # 找到左子树（节点值全部小于根节点j）
            while postorder[p] < postorder[j]:
                p += 1
            m = p  # 根节点的右子节点
            # 后续看p是否等于j，验证右子树是否都大于根节点;
            # 不用验证左子树，因为由第一个while挑选出来的左子树已经满足全都小于根节点j
            while postorder[p] > postorder[j]:  
                p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)  # 递归继续判断子树
        return recur(0, len(postorder) - 1)
