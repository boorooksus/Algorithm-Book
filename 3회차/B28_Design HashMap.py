import sys
from typing import Optional


class MyNode:
    def __init__(self, key: int = -sys.maxsize, value: int = -1, next: Optional = None):
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = MyNode()

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        node = self.root
        while node.next and key >= node.next.key:
            node = node.next

        if node.key == key:
            node.value = value
        else:
            target = MyNode(key, value)
            node.next, target.next = target, node.next

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        node = self.root

        while node:
            if node.key == key:
                return node.value
            elif node.key > key:
                break
            node = node.next

        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        node = self.root

        while node and node.next:
            if node.next.key == key:
                node.next = node.next.next
            elif node.next.key > key:
                break
            node = node.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)