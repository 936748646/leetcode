# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        l = ListNode(stack.pop())
        head = l
        while stack:
            head.next = ListNode(stack.pop())
            head = head.next
        return l
