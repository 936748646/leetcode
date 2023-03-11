# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 快慢指针，ptr2先走n步，然后ptr1和ptr2一起走
        if not head.next:  # 链表长度为1
            return None
        ptr1, ptr2 = head, head
        for i in range(n):
            ptr2 = ptr2.next
        if not ptr2:  # 链表长度=n，直接删除head即可
            return head.next
        while ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr1.next = None if n == 1 else ptr1.next.next  # n=1时ptr1.next.next会报错
        return head

# 编写过程中导致报错的几个特殊情况：①链表长度为1；②链表长度=n；③n=1
