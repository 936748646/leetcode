#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.check(root)
    def check(self, root, minVal = float('-inf'), maxVal = float('inf')):
        if not root:
            return True
        if root.val >= maxVal or root.val <= minVal:
            return False
        return self.check(root.left, minVal, root.val) and self.check(root.right, root.val, maxVal)
# @lc code=end

