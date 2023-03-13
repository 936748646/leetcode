# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 两指针从A、B同步往后走，遍历完A就从B头开始走，遍历完B就从A头开始走，最终相遇的节点就是相交节点
        ptr1, ptr2 = headA, headB
        while ptr1 != ptr2:
            if not ptr1.next and not ptr2.next:
                return None
            if ptr1.next:
                ptr1 = ptr1.next
            else:
                ptr1 = headB
            if ptr2.next:
                ptr2 = ptr2.next
            else:
                ptr2 = headA
        return ptr1
