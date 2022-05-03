#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) > 0:
            root = TreeNode(preorder[0])
            root_index = inorder.index(preorder[0])
            # 前序先遍历root的左子节点，中序root位置之前也是左子节点
            root.left = self.buildTree(preorder[1: root_index + 1], inorder[: root_index])
            root.right = self.buildTree(preorder[root_index + 1:], inorder[root_index + 1:])
        else:
            root = None
        return root
# @lc code=end

