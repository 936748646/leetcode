# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        temp = head
        l = 0
        while temp:
            l += 1
            temp = temp.next
        for i in range(l - k):
            head = head.next
        return head
