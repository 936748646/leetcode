# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # fast、slow两指针相遇时根据走过的步数（f、s）确定环入口节点
        # 设链表共有a+b个节点，a为链表头到环入口的节点数（不包含入口），b为环的节点数
        # 所有走到环入口时的步数均为：a+nb
        # f=2s,f=s+nb，得s=nb。因此slow再走a步就到达环入口
        fast, slow = head, head
        while True:
            if not fast or not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        fast = head
        while fast != slow:  # 再让slow走a步方法：另一个指针从head开始同步向后走，相遇即为环入口
            fast = fast.next
            slow = slow.next
        return fast
