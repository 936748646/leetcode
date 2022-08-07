# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 设root为所求最近公共祖先，则p、q只可能为以下3种情况之一：
        # 1.p、q分别在root的左右子树中
        # 2.p=root，q在root的子树中
        # 3.q=root，p在root的子树中
        while root:
            if root.val < p.val and root.val < q.val: root = root.right
            elif root.val > p.val and root.val > q.val: root = root.left
            else: break
        return root
