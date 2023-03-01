# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 两指针同步向前走，走到头就返回到对方链表头继续走，直到两指针相遇
        # 此时两指针都走了l1+l2+c（l1、l2：A、B的非公有部分长度；c：共有部分长度）
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
