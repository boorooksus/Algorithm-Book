class ListNode:
    def __init__(self, val: int = -1):
        self.val = val
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.head.right, self.tail.left = self.tail, self.head
        self.len, self.k = 0, k

    def enQueue(self, value: int) -> bool:
        if self.len != self.k:
            self.len += 1
            new = ListNode(value)
            new.left, new.right = self.tail.left, self.tail
            self.tail.left.right, self.tail.left = new, new
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.len > 0:
            self.len -= 1
            self.head.right.right.left, self.head.right = self.head, self.head.right.right
            return True
        else:
            return False

    def Front(self) -> int:
        return self.head.right.val if self.len > 0 else -1

    def Rear(self) -> int:
        return self.tail.left.val if self.len > 0 else -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()