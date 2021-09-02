from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return l1 or l2

        root = node = ListNode(None)

        while l1 or l2:
            if (l1 and not l2) or (l1 and l2 and l1.val < l2.val):
                node.next = l1
                l1 = l1.next
            elif (not l1 and l2) or (l1 and l2 and l1.val >= l2.val):
                node.next = l2
                l2 = l2.next

            node = node.next

        return root.next
