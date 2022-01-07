from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev = head
        head = head.next
        odd, even = prev, head

        while head and head.next:
            prev.next, head.next = head.next, head.next.next
            prev, head = prev.next, head.next

        prev.next = even

        return odd
    