# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 3种情况和上题相同
        if not root or root == p or root == q: return root  # 递归终止条件
        # 递归遍历左子树，返回如果左子树中找到了p或q
        left = self.lowestCommonAncestor(root.left, p, q)
        # 递归遍历右子树，返回如果右子树中找到了p或q
        right = self.lowestCommonAncestor(root.right, p, q)
        # 如果左子树中没有找到p或q，则上面递归找到的right是所找的最近公共祖先
        if not left: return right
        # 如果右子树中没有找到p或q，则上面递归找到的left是所找的最近公共祖先
        if not right: return left
        return root  # 如果左子树和右子树同时找到了p和q，证明p、q分别在root两侧，root即为最近公共祖先
