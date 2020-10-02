class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head


    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.len < self.k:
            self.len += 1
            self._add(self.head, ListNode(value))
            return True
        else:
            return False


    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.len < self.k:
            self.len += 1
            self._add(self.tail.left, ListNode(value))
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.len > 0:
            self.len -= 1
            self._del(self.head)
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.len > 0:
            self.len -= 1
            self._del(self.tail.left.left)
            return True
        else:
            return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.len > 0:
            return self.head.right.val
        else:
            return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.len > 0:
            return self.tail.left.val
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return True if self.len == 0 else False

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return True if self.len == self.k else False

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

# leetcode: 641
# ListNode로 구현
