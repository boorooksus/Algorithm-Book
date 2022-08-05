from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        root = prev = ListNode()
        node = head
        prev.next = node

        while node and node.next:
            next, prev.next, node.next.next = node.next.next, node.next, node
            node.next = next
            prev, node = node, node.next

        return root.next


