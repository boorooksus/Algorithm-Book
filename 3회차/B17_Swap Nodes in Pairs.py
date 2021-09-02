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

        root = node = ListNode(None)
        root.next = head

        while node and node.next and node.next.next:
            left, right = node.next, node.next.next
            temp, node.next, right.next = right.next, right, left
            left.next, node = temp, node.next.next

        return root.next
