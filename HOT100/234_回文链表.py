# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        l = []
        while head:
            l.append(head.val)
            head = head.next
        return l == l[::-1]  # 反转列表进行比较
        
