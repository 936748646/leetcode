#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        l = len(stack) / 2
        left = 0
        right = len(stack) - 1
        while left < right:
            if stack[left] != stack[right]:
                return False
            left += 1
            right -= 1
        return True

# @lc code=end

