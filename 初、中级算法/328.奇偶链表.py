#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None or head.next.next is None:
            return head
        odd_head = head
        odd_cur = odd_head
        even_head = head.next
        even_cur = even_head
        while even_cur and even_cur.next:
            odd_cur.next = odd_cur.next.next
            even_cur.next = even_cur.next.next
            odd_cur = odd_cur.next
            even_cur = even_cur.next
        odd_cur.next = even_head
        return odd_head
# @lc code=end

