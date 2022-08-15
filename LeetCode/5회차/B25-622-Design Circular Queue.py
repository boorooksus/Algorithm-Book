from collections import deque


class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.start = 0
        self.cnt = 0
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.cnt == self.size:
            return False
        self.q[(self.start + self.cnt) % self.size] = value
        self.cnt += 1
        return True

    def deQueue(self) -> bool:
        if self.cnt == 0:
            return False
        self.start = (self.start + 1) % self.size
        self.cnt -= 1
        return True

    def Front(self) -> int:
        if self.cnt == 0:
            return -1
        return self.q[self.start]

    def Rear(self) -> int:
        if self.cnt == 0:
            return -1
        return self.q[(self.start + self.cnt - 1) % self.size]

    def isEmpty(self) -> bool:
        return self.cnt == 0

    def isFull(self) -> bool:
        return self.cnt == self.size

# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
param_1 = obj.enQueue(1)
param_1 = obj.enQueue(2)
param_1 = obj.enQueue(3)
param_1 = obj.enQueue(4)
# param_3 = obj.Front()
param_4 = obj.Rear()
print(param_4)
# param_5 = obj.isEmpty()
param_6 = obj.isFull()
param_2 = obj.deQueue()
print(param_2)
param_1 = obj.enQueue(4)
param_4 = obj.Rear()
print(param_4)


"""
"deQueue","enQueue","Rear"]
[],[4],[]]
"""