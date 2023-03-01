# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        count = 0
        while l1:
            num1 += l1.val * pow(10, count)
            count += 1
            l1 = l1.next
        count = 0
        while l2:
            num2 += l2.val * pow(10, count)
            count += 1
            l2 = l2.next
        s = list(str(num1 + num2))
        head = ListNode(int(s.pop()))
        res = head
        while s:
            head.next = ListNode(int(s.pop()))
            head = head.next
        return res
