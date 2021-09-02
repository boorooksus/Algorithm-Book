from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        root = prev = ListNode(None)
        root.next = head

        while head and head.next:
            b, head.next = head.next, head.next.next
            b.next, prev.next = head, b
            head, prev = head.next, prev.next.next

        return root.next
