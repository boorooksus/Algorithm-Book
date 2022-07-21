class MyStack:

    def __init__(self):
        self.qa = []
        self.qb = []

    def push(self, x: int) -> None:
        self.qa.append(x)

    def pop(self) -> int:
        while len(self.qa) > 1:
            self.qb.append(self.qa.pop(0))
        res = self.qa.pop()
        while self.qb:
            self.qa.append(self.qb.pop(0))
        return res

    def top(self) -> int:
        while len(self.qa) > 1:
            self.qb.append(self.qa.pop(0))
        res = self.qa.pop()
        self.qb.append(res)
        while self.qb:
            self.qa.append(self.qb.pop(0))
        return res

    def empty(self) -> bool:
        return len(self.qa) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
