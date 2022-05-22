"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    # 不能直接一次遍历复制，因为无法构建random
    # 要先遍历一遍复制val，再遍历一遍复制next、random
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        dic = {}
        cur = head
        # 先构建原节点-新节点映射（新节点暂时只存val）
        # 原节点：cur
        # 新节点：dic[cur]
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        return dic[head]
