class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.k, self.size = k, 0
        self.head, self.tail = ListNode(None), ListNode(None)
        self.head.left = self.head.right = self.tail
        self.tail.left = self.tail.right = self.head

    def _add(self, left: ListNode, node: ListNode):
        right = left.right
        left.right, node.left = node, left
        node.right, right.left = right, node

    def _del(self, node: ListNode):
        left, right = node.left, node.right
        left.right, right.left = right, left

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.size += 1
        self._add(self.head, ListNode(value))
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.size += 1
        self._add(self.tail.left, ListNode(value))
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.size -= 1
        self._del(self.head.right)
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.size -= 1
        self._del(self.tail.left)
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return -1 if self.isEmpty() else self.head.right.val

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return -1 if self.isEmpty() else self.tail.left.val

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.head.right == self.tail

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.k == self.size


obj = MyCircularDeque(3)
obj.insertLast(1)
obj.insertLast(2)
obj.insertFront(3)
# obj = MyCircularDeque(5)
# obj.insertFront(7)
# obj.insertLast(0)
# print(obj.getFront())
# # obj.isEmpty()
# # obj.deleteFront()
# obj.insertLast(3)
# print(obj.getFront())
# obj.insertLast(9)
# print(obj.getFront())
# obj.getRear()
# print(obj.getFront())
# print(obj.getFront())
# obj.deleteLast()
# print(obj.getRear())

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()