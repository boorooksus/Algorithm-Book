from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        root = prev = ListNode(None)
        root.next = head
        cur = 1

        while cur < left:
            prev, head = prev.next, head.next
            cur += 1

        while head and head.next and cur < right:
            rev, head.next, rev.next = head.next, head.next.next, prev.next
            prev.next = rev
            cur += 1

        return root.next
