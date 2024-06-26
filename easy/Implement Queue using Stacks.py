class MyQueue:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        while self.queue1:
            self.queue2.append(self.queue1.pop())

        self.queue2.append(x)
        while self.queue2:
            self.queue1.append(self.queue2.pop())

    def pop(self) -> int:
        if self.queue1:
            return self.queue1.pop()

    def peek(self) -> int:
        if self.queue1:
            return self.queue1[-1]

    def empty(self) -> bool:
        if not self.queue1:
            return True

        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()