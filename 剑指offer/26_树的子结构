# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 先序遍历A每个节点，判断以A中每个节点为根节点的子树是否包含B
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        # 判断以A中节点为根节点的子树是否包含B
        def recur(A, B):
            if not B:
                return True
            if not A or A.val != B.val:
                return False
            return recur(A.left, B.left) and recur(A.right, B.right)
        # 先序遍历，3种情况：
        # 1. 以节点A为根节点的子树包含B
        # 2. B是A左子树的子结构
        # 3. B是A右子树的子结构
        if recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B):
            return True
        return False
