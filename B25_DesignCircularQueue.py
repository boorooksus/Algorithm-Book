from collections import deque

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.dq = deque()
        self.size = k


    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if len(self.dq) == self.size:
            return False
        self.dq.append(value)
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if not self.dq:
            return False
        self.dq.popleft()
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if not self.dq:
            return -1
        else:
            return self.dq[0]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if not self.dq:
            return -1
        else:
            return self.dq[-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.dq:
            return False
        else:
            return True

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if len(self.dq) == self.size:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

# leetcode: 622
# 포인터를 이용해서 풀어볼 것!
