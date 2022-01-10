from typing import Optional, List
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = node = ListNode(None)
        hq = []

        for i, head in enumerate(lists):
            if head:
                heapq.heappush(hq, (head.val, i, head))

        while hq:
            val, idx, node.next = heapq.heappop(hq)
            node = node.next

            if node.next:
                heapq.heappush(hq, (node.next.val, idx, node.next))

        return root.next
