# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # 分治，分别把1...n做根节点，再左右子树递归。思路类似241题，根节点类似241题的运算符
        def buildTrees(left, right):
            res = []
            if left > right: return [None]  # 可能当前节点左右没有子节点了，要记为null
            for i in range(left, right + 1):
                left_trees = buildTrees(left, i - 1)
                right_trees = buildTrees(i + 1, right)
                for l in left_trees:  # 以i做根节点，逐一连结左右子树的各种可能情况
                    for r in right_trees:
                        cur_tree = TreeNode(i)
                        cur_tree.left, cur_tree.right = l, r
                        res.append(cur_tree)
            return res
        return buildTrees(1, n)
