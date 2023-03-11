# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if list1 else list2
        head = ListNode()
        res = head
        while list1 and list2:
            if list1.val <= list2.val:
                head.val = list1.val
                head.next = ListNode()
                head = head.next
                list1 = list1.next
            else:
                head.val = list2.val
                head.next = ListNode()
                head = head.next
                list2 = list2.next
        last = list1 if list1 else list2  # 这里其实是head=last即可，但答案不对，不知道为什么，只能先处理当前节点head.val = last.val，再head.next = last.next
        if last:
            head.val = last.val
            head.next = last.next
            head = head.next
            last = last.next
        return res
