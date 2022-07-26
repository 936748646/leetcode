# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            if left == -1: return -1
            right = dfs(root.right)
            if right == -1: return -1
            # 若当前子树满足平衡条件，则返回当前子树深度，继续向上比较子树
            return max(left, right) + 1 if abs(left - right) <= 1 else -1
        return dfs(root) != -1
