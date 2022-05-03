#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.dfs(root, None)
        return root
    def dfs(self, cur, next):
        if not cur:
            return
        cur.next = next
        self.dfs(cur.left, cur.right)
        self.dfs(cur.right, None if cur.next == None else cur.next.left)
# @lc code=end

