class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None for _ in range(k)]
        self.k = k
        self.p1, self.p2 = 0, 0

    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.k
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.k
            return True

    def Front(self) -> int:
        return self.q[self.p1] if self.q[self.p1] is not None else -1

    def Rear(self) -> int:
        return self.q[self.p2 - 1] if self.q[self.p2 - 1] is not None else -1

    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()