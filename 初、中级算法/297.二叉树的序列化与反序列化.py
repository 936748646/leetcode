#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        self.preorder(root, res)
        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        node_list = data.split(',')
        node_list.reverse()
        return self.depreorder(node_list)


    def preorder(self, root, res):
        if not root:
            res.append('None')
            return
        res.append(str(root.val))
        self.preorder(root.left, res)
        self.preorder(root.right, res)
    

    def depreorder(self, node_list):
        if not node_list:
            return
        if node_list[-1] == 'None':
            node_list.pop()
            return
        root = TreeNode(int(node_list[-1]))
        node_list.pop()
        root.left = self.depreorder(node_list)
        root.right = self.depreorder(node_list)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

