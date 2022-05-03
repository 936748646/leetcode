#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.travel(root, res, 0)
        return res
    def travel(self, root, res, level):
        if not root:
            return
        if len(res) <= level:
            res.append([])
        cur = res[level]  # 操作层
        if level % 2 == 0:
            cur.append(root.val)
        else:
            cur.insert(0, root.val)
        self.travel(root.left, res, level + 1)
        self.travel(root.right, res, level + 1)
# @lc code=end

