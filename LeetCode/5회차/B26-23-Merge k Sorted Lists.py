from typing import Optional, List
from heapq import heappop, heappush


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(hq):
            if not hq:
                return None
            _, idx, node = heappop(hq)
            if node.next:
                heappush(hq, [node.next.val, idx, node.next])
            node.next = merge(hq)
            return node

        hq = []
        for i, node in enumerate(lists):
            if node:
                heappush(hq, [node.val, i, node])
        return merge(hq)
