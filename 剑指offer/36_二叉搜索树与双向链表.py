"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # 中序遍历：左子树-根-右子树（在根的位置访问）
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            if self.pre:
                self.pre.right = cur
                cur.left = self.pre
            else:  # 当前节点无前驱节点，为head
                self.head = cur
            self.pre = cur
            dfs(cur.right)
        if not root:
            return
        self.pre = None
        dfs(root)
        # 处理首尾节点相连
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head
