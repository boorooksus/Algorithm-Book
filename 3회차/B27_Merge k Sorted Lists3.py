from typing import Optional, List
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode()
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            _, index, result.next = heapq.heappop(heap)

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, index, result.next))

        return root.next


x, y, z = ListNode(1), ListNode(5), ListNode(10)
a, b, c = ListNode(2), ListNode(7), ListNode(15)
x.next, y.next = y, z
a.next, b.next = b, c
Solution().mergeKLists([x, a])
