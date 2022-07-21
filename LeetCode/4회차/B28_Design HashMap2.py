from collections import defaultdict


class ListNode:
    def __init__(self, key: int = None, val: int = None):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:

    def __init__(self):
        self.table = defaultdict(ListNode)
        self.size = 1000

    def put(self, key: int, value: int) -> None:
        idx = key % self.size
        p = self.table[idx]

        if p.key is None:
            self.table[idx] = ListNode(key, value)
            return

        while p:
            if p.key == key:
                p.val = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        idx = key % self.size
        p = self.table[idx]

        if p.val is None:
            return -1

        while p:
            if p.key == key:
                return p.val
            p = p.next

        return -1

    def remove(self, key: int) -> None:
        idx = key % self.size

        p = self.table[idx]

        if p.val is None:
            return

        if p.key == key:
            self.table[idx] = p.next if p.next else ListNode()
            return

        while p.next:
            if p.next.key == key:
                p.next = p.next.next
                return
            p = p.next

#
# obj = MyHashMap()
# print(obj.put(1, 1))
# print(obj.put(2, 2))
# print(obj.get(1))
# print(obj.get(3))
# print(obj.put(2, 1))
# print(obj.get(2))
# print(obj.remove(2))
# print(obj.get(2))

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)