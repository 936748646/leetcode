#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = 0
        lenB = 0
        nodeA = headA
        nodeB = headB
        while nodeA:
            nodeA = nodeA.next
            lenA += 1
        while nodeB:
            nodeB = nodeB.next
            lenB += 1
        if lenA > lenB:
            count = lenA - lenB
            while count != 0:
                headA = headA.next
                count -= 1
        elif lenA < lenB:
            count = lenB - lenA
            while count != 0:
                headB = headB.next
                count -= 1
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
# @lc code=end

