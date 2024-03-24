class MinStack:
    def __init__(self):
        self.ori_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.ori_stack.append(val)
        if len(self.min_stack) == 0 or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.ori_stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.ori_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]