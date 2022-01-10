class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:

    def __init__(self):
        self.root = ListNode(None, None)

    def put(self, key: int, value: int) -> None:
        node = self.root

        while node.next:
            if node.next.key == key:
                node.next.val = value
                return
            elif key < node.next.key:
                break
            node = node.next

        next, new = node.next, ListNode(key, value)
        node.next, new.next = new, next

    def get(self, key: int) -> int:
        node = self.root
        while node.next:
            if node.next.key == key:
                return node.next.val
            elif node.next.key > key:
                break
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        node = self.root
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            elif node.next.key > key:
                return
            node = node.next


obj = MyHashMap()
obj.put(1, 1)
obj.put(2, 2)
obj.get(1)
obj.get(3)
obj.put(2, 1)
obj.get(2)
obj.remove(2)
obj.get(2)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)