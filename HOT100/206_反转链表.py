# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # 原地反转：双指针，一个从None开始，一个从head开始，同步向后移，ptr2的指针反过来指向ptr1
        ptr1, ptr2 = None, head
        while ptr2:
            tmp = ptr2.next
            ptr2.next = ptr1
            ptr1 = ptr2
            ptr2 = tmp
        return ptr1
