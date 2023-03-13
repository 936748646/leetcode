# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        # 将链表从中间断开，mid为第二部分的头结点
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None
        # 递归砍链表
        left, right = self.sortList(head), self.sortList(mid)  # sortList返回res.next=None时结束递归，证明已经砍到只有单个节点了
        # 归并
        h = res = ListNode()
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next

# 递归我肯定写不出来，但是迭代又不想写了
