class MinStack:
    def __init__(self):
        self.stack = []
        self.min_nums = []

    def push(self, val: int) -> None:
        if self.min_nums and val <= self.min_nums[-1]:
            self.min_nums.append(val)

        if not self.min_nums:
            self.min_nums.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.min_nums[-1]:
                self.min_nums.pop()

            return val

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.stack:
            return self.min_nums[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()