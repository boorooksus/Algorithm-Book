from typing import Optional, List
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hq = []
        for head in lists:
            while head:
                heapq.heappush(hq, head.val)
                head = head.next

        vals = heapq.nsmallest(len(hq), hq)

        root = cur = ListNode(None)
        for val in vals:
            cur.next = ListNode(val)
            cur = cur.next

        return root.next


