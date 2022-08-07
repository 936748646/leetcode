# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, queue, flag = [], collections.deque(), 0
        queue.append(root)
        while queue:
            layer = []
            for i in range(len(queue)):
                node = queue.popleft()
                layer.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if flag:
                res.append(layer[::-1])
                flag = 0
            else:
                res.append(layer)
                flag = 1
        return res
