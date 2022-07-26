# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if not root: return
            dfs(root.right)
            # 在中序遍历基础上更改成判断是否访问到了第k大的元素，如果是就直接return节省时间
            self.tmp += 1
            if self.tmp == k: 
                self.res = root.val
                return
            dfs(root.left)
        self.tmp = 0
        dfs(root)
        return self.res
