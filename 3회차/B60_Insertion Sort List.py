# Definition for singly-linked list.
import sys
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        parent = cur = ListNode(None)

        while head:

            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            if head and cur.next.val > head.val:
                cur = parent

        return parent.next






