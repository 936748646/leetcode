class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []


    def push(self, x: int) -> None:
        self.stack.append(x)


    def pop(self) -> None:
        self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]


    def min(self) -> int:
        return min(self.stack)
