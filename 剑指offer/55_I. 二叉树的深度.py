# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 后序遍历
        if not root: return 0
        res = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        return res
