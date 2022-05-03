#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s != '+' and s != '-' and s != '*' and s != '/':
                stack.append(int(s))
            else:
                b = stack.pop(-1)
                a = stack.pop(-1)
                if s == '+':
                    a += b
                elif s == '-':
                    a -= b
                elif s == '*':
                    a *= b
                elif s == '/':
                    a = int(a / b)  # //是整体向下取整，如-6.5取-7；而int(/)是绝对值的向下取整，如-6.5取-6
                stack.append(a)
        return stack[0]
# @lc code=end

