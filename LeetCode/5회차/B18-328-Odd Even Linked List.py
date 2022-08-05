from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_root = odd = ListNode()
        even_root = even = ListNode()

        while head:
            odd.next = head
            odd, head = odd.next, head.next
            if not head:
                break
            even.next = head
            even, head = even.next, head.next

        odd.next, even.next = even_root.next, None
        return odd_root.next
