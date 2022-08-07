class Solution:
    # 重新压栈，在压栈同时判断是否符合出栈顺序
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0  # popped计数
        stack = []
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        if stack:
            return False
        return True
