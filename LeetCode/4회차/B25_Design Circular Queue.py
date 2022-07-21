class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0 for _ in range(k + 2)]
        self.first = 0
        self.last = 1
        self.size = k + 2

    def enQueue(self, value: int) -> bool:
        if (self.last + 1) % self.size == self.first:
            return False

        self.q[self.last] = value
        self.last = (self.last + 1) % self.size
        return True

    def deQueue(self) -> bool:
        if (self.first + 1) % self.size == self.last:
            return False

        self.first = (self.first + 1) % self.size
        return True

    def Front(self) -> int:
        if (self.first + 1) % self.size == self.last:
            return -1
        return self.q[(self.first + 1) % self.size]

    def Rear(self) -> int:
        if (self.first + 1) % self.size == self.last:
            return -1
        return self.q[(self.last + self.size - 1) % self.size]

    def isEmpty(self) -> bool:
        return (self.first + 1) % self.size == self.last

    def isFull(self) -> bool:
        return (self.last + 1) % self.size == self.first


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
