class MyQueue:

    def __init__(self):
        self.sa = []
        self.sb = []

    def push(self, x: int) -> None:
        while self.sa:
            self.sb.append(self.sa.pop())
        self.sa.append(x)
        while self.sb:
            self.sa.append(self.sb.pop())

    def pop(self) -> int:
        return self.sa.pop()

    def peek(self) -> int:
        return self.sa[-1]

    def empty(self) -> bool:
        return len(self.sa) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()