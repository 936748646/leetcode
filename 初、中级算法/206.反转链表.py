#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        stack = []
        if not head:
            return head
        while head:
            stack.append(head.val)
            head = head.next
        l = ListNode()
        head = l
        for i in range(len(stack) - 1, -1, -1):
            node = ListNode(stack[i])
            head.next = node
            head = head.next
        return l.next

# @lc code=end

