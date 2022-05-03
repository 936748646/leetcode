#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in dict and stack and stack[-1] == dict[i]:
                stack.pop()
            else:
                stack.append(i)
        if stack:
            return False
        else:
            return True
# @lc code=end

