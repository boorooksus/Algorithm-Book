from typing import Optional, List
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = ListNode()
        hq = []
        idx = 0

        for node in lists:
            while node:
                heapq.heappush(hq, (node.val, idx, node))
                node = node.next
                idx += 1

        node = root
        while hq:
            _, _, node.next = heapq.heappop(hq)
            node = node.next
        return root.next


x, y, z = ListNode(1), ListNode(5), ListNode(10)
a, b, c = ListNode(2), ListNode(7), ListNode(15)
x.next, y.next = y, z
a.next, b.next = b, c
Solution().mergeKLists([x, a])
