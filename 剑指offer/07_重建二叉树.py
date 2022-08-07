# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 和105题相同
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder:
            root = TreeNode(preorder[0])
            root_index = inorder.index(preorder[0])
            root.left = self.buildTree(preorder[1: root_index + 1], inorder[: root_index])
            root.right = self.buildTree(preorder[root_index + 1:], inorder[root_index + 1:])
        else:
            return None

        return root
