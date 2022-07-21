class ListNode:
    def __init__(self, val: int = -1):
        self.val = val
        self.next = None


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.root = ListNode()
        self.root.next = self.root
        self.left = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.left == 0:
            return False

        self.left -= 1

        node = ListNode(value)
        node.next, self.root.next = self.root.next, node

        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.left == 0:
            return False

        self.left -= 1

        node = ListNode(value)
        cur = self.root
        while cur.next and cur.next != self.root:
            cur = cur.next

        node.next, cur.next = cur.next, node

        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.root.next == self.root:
            return False

        self.left += 1

        self.root.next = self.root.next.next
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.root.next == self.root:
            return False

        self.left += 1

        node, prev = self.root, None
        while node.next and node.next != self.root:
            prev = node
            node = node.next
        prev.next = self.root

        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.root.next.val

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        node = self.root
        while node.next and node.next != self.root:
            node = node.next
        return node.val

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return True if self.root.next == self.root else False

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.left == 0

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